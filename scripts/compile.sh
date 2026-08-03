#!/usr/bin/env bash
#
# compile.sh — build the ByteBoost LaTeX PDFs.
#
# Usage:
#   bash scripts/compile.sh              # description + abstract
#   bash scripts/compile.sh description  # project description only
#   bash scripts/compile.sh abstract     # participant abstract only
#   bash scripts/compile.sh clean        # remove aux files (keeps PDFs)
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

DESC_DIR="$REPO_ROOT/documents/description"
ABS_DIR="$REPO_ROOT/documents/abstract"
DESC_MAIN="byteboost_project_description"
ABS_MAIN="byteboost_abstract"

compile_description() {
  echo "Compiling $DESC_MAIN ..."
  (
    cd "$DESC_DIR"
    pdflatex -interaction=nonstopmode "$DESC_MAIN"
    bibtex "$DESC_MAIN"
    pdflatex -interaction=nonstopmode "$DESC_MAIN"
    pdflatex -interaction=nonstopmode "$DESC_MAIN"
  )
  echo "Wrote $DESC_DIR/$DESC_MAIN.pdf"
}

compile_abstract() {
  echo "Compiling $ABS_MAIN ..."
  (
    cd "$ABS_DIR"
    pdflatex -interaction=nonstopmode "$ABS_MAIN"
  )
  echo "Wrote $ABS_DIR/$ABS_MAIN.pdf"
}

clean_aux() {
  echo "Cleaning aux files ..."
  rm -f "$DESC_DIR/$DESC_MAIN".{aux,bbl,blg,log,out} \
        "$ABS_DIR/$ABS_MAIN".{aux,log,out}
  echo "Done (PDFs kept)."
}

target="${1:-all}"

case "$target" in
  description) compile_description ;;
  abstract)    compile_abstract ;;
  all)
    compile_description
    compile_abstract
    ;;
  clean)       clean_aux ;;
  *)
    echo "Usage: $0 [all|description|abstract|clean]" >&2
    exit 1
    ;;
esac
