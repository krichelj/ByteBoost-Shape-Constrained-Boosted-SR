#!/usr/bin/env bash
#
# compile.sh: build the ByteBoost project-description PDF.
#
# Usage:
#   bash scripts/compile.sh          # project description
#   bash scripts/compile.sh clean    # remove aux files (keeps PDF)
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

DESC_DIR="$REPO_ROOT/documents/description"
DESC_MAIN="byteboost_project_description"

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

clean_aux() {
  echo "Cleaning aux files ..."
  rm -f "$DESC_DIR/$DESC_MAIN".{aux,bbl,blg,log,out}
  echo "Done (PDF kept)."
}

target="${1:-all}"

case "$target" in
  all|description) compile_description ;;
  clean)           clean_aux ;;
  *)
    echo "Usage: $0 [all|description|clean]" >&2
    exit 1
    ;;
esac
