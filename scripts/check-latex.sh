#!/usr/bin/env bash
#
# check-latex.sh: recompile documents/description/byteboost_project_description
# from source and reject the build if it produces ANY LaTeX error,
# LaTeX/package/class/font warning, over/underfull box, or BibTeX warning/error.
#
# It deliberately never inspects the committed *.pdf. It copies only the
# source (*.tex/*.bib, plus any local *.bst/*.cls/*.sty) into a throwaway
# temp dir, builds from scratch to convergence, and judges the FINAL log
# plus the BibTeX .blg. Exit 0 = clean, exit 1 = errors/warnings found,
# exit 2 = toolchain missing.
#
set -uo pipefail

DOC="byteboost_project_description"
SRC_DIR="documents/description"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

if ! command -v latexmk >/dev/null 2>&1; then
  echo "check-latex: latexmk not found; a TeX Live install is required." >&2
  exit 2
fi

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

# Copy ONLY source inputs: never the PDF, never stale aux files. Building
# from a clean slate is the whole point: the verdict must not depend on any
# previously compiled artifact.
shopt -s nullglob
for f in "$REPO_ROOT/$SRC_DIR"/*.tex "$REPO_ROOT/$SRC_DIR"/*.bib \
         "$REPO_ROOT/$SRC_DIR"/*.bst "$REPO_ROOT/$SRC_DIR"/*.cls \
         "$REPO_ROOT/$SRC_DIR"/*.sty; do
  cp "$f" "$WORK"/
done
shopt -u nullglob

cd "$WORK" || exit 2

# Full, converged, from-scratch build. latexmk runs pdflatex + bibtex as many
# times as needed, so intermediate "rerun / labels may have changed" messages
# resolve before we inspect the final log. -halt-on-error makes hard errors
# fail the build immediately; warnings do NOT stop latexmk, so we parse for
# them explicitly below.
latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error "$DOC.tex" \
  >build.transcript 2>&1
build_rc=$?

log="$DOC.log"
blg="$DOC.blg"
status=0

if [ "$build_rc" -ne 0 ]; then
  echo "REJECTED: LaTeX build did not complete cleanly (latexmk exit $build_rc)."
  echo "----- build transcript (last 30 lines) -----"
  tail -n 30 build.transcript
  echo "---------------------------------------------"
  status=1
fi

# 1) Hard TeX / LaTeX errors in the final log.
if [ -f "$log" ] && \
   grep -nE '^!|Emergency stop|Fatal error occurred|LaTeX Error|pdfTeX error' \
        "$log" > errors.txt; then
  echo "REJECTED: LaTeX errors:"
  sed 's/^/    /' errors.txt
  status=1
fi

# 2) LaTeX / font / package / class warnings and over/underfull boxes.
#    Matches LaTeX's structured warning markers only, so benign package
#    banners containing the word "warning" are not false positives.
if [ -f "$log" ] && \
   grep -nE 'LaTeX Warning:|LaTeX Font Warning:|Package [A-Za-z0-9@]+ Warning:|Class [A-Za-z0-9@]+ Warning:|^(Overfull|Underfull) \\[hv]box' \
        "$log" > warnings.txt; then
  echo "REJECTED: LaTeX warnings:"
  sed 's/^/    /' warnings.txt
  status=1
fi

# 3) BibTeX warnings / errors from the .blg. The .blg contains the token
#    "warning$" in its function-call stats, so match the real markers only:
#    per-warning "Warning--" lines and the "(There was/were N ...)" summary.
if [ -f "$blg" ] && \
   grep -nE 'Warning--|\(There (was|were) [0-9]+ (warning|error)' \
        "$blg" > bibtex.txt; then
  echo "REJECTED: BibTeX warnings/errors:"
  sed 's/^/    /' bibtex.txt
  status=1
fi

if [ "$status" -eq 0 ]; then
  echo "OK: $DOC compiled cleanly from scratch with no errors and no warnings."
fi
exit "$status"
