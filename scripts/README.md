# Build guard

`check-latex.sh` recompiles `byteboost_project_description` **from source** and
exits non-zero if the build produces any LaTeX error, LaTeX/font/package/class
warning, over/underfull box, or BibTeX warning. It never inspects the committed
PDF: it copies only the `.tex`/`.bib` (and any local `.bst`/`.cls`/`.sty`) into a
temporary directory, builds to convergence with `latexmk`, and judges the final
`.log` and the BibTeX `.blg`.

```bash
bash scripts/check-latex.sh   # exit 0 = clean, 1 = errors/warnings, 2 = no TeX Live
```

## Where it runs

- **CI (authoritative):** `.github/workflows/latex-guard.yml` runs it in the
  official `texlive/texlive` container on every push and pull request to `main`.
  Branch protection requires the `compile-check` status, so a change that
  compiles with errors or warnings cannot be merged.
- **Locally (optional):** enable the pre-push hook once per clone —

  ```bash
  git config core.hooksPath githooks
  ```

  The push is then rejected if the document does not compile cleanly. If TeX
  Live is not installed locally the hook steps aside and lets CI enforce.
