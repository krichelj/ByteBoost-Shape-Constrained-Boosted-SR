# ByteBoost 2026

**Shape-Constrained Boosted Symbolic Regression for Interpretable Neural Scaling Laws: A Cross-Testbed Investigation**

Workshop project description for [ByteBoost 2026](https://www.stonybrook.edu/ookami/ByteBoost.php) (ACCESS cyberinfrastructure testbeds). Discover neural scaling-law formulas with symbolic regression, while certifying physical priors (monotonicity, diminishing returns, positivity, irreducible floor, power-law decay) via interval-arithmetic forward-mode AD, across Cerebras CS-3 (Neocortex) pretraining and AmpereOne (AMA27) search.

## Documents

- [Project description](documents/description/byteboost_project_description.pdf)

## Student skeleton

Implement the method in [`src/`](src/). Each subpackage maps to a section of the project description (setup, axioms, certificates, boosting, hard/soft paths, modeling track, …). Stubs use the description’s notation and raise `NotImplementedError` — see [`src/README.md`](src/README.md) for the full map and suggested order.

## Build

```bash
bash scripts/compile.sh
# or
make
```

Requires a standard TeX Live / MacTeX install (`pdflatex`, `bibtex`, and the packages listed in the preamble). Pass `description`, `abstract`, or `clean` to compile one document or remove aux files (`make` accepts the same targets).

## Build guard

`make` / `compile.sh` builds the PDFs; `make check` is a stricter quality gate. It copies only the `.tex`/`.bib` sources into a temp directory, rebuilds from scratch with `latexmk`, and rejects the change if the log has any LaTeX error, package/font/class warning, over/underfull box, or BibTeX warning. It never trusts the committed PDF.

```bash
make check
```

Optionally run the same gate before every push:

```bash
git config core.hooksPath githooks
```

If TeX Live is missing locally, the pre-push hook skips.

## Related

- Scaling-grid checkpoints: [`leibnitz-lab/colinear_scaling_models`](https://huggingface.co/datasets/leibnitz-lab/colinear_scaling_models)
- Method: shape-constrained boosted SR with hard (IA certificates) and soft (violation penalties) paths

## License

[MIT](LICENSE).
