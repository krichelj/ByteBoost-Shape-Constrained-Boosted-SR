# ByteBoost 2026

**Shape-Constrained Boosted Symbolic Regression for Interpretable Neural Scaling Laws: A Cross-Testbed Investigation**

Workshop project for [ByteBoost 2026](https://www.stonybrook.edu/ookami/ByteBoost.php) (ACCESS cyberinfrastructure testbeds). Discover neural scaling-law formulas with symbolic regression, while certifying physical priors (monotonicity, diminishing returns, positivity, irreducible floor, power-law decay) via interval-arithmetic forward-mode AD, across Cerebras CS-3 (Neocortex) pretraining and AmpereOne (AMA27) search.

## Documents

- [Project description](documents/description/byteboost_project_description.pdf)

## Student skeleton

Implement the method in [`src/`](src/), organized into five packages (`scaling`, `constraints`, `search`, `modeling`, `systems`). Stubs use the description’s notation and raise `NotImplementedError` — see [`src/README.md`](src/README.md) for the full map and suggested order.

Run Python from the repository root so imports like `from src.scaling.setup…` resolve.

## Repository layout

```
documents/description/   # LaTeX source, bibliography, committed PDF
src/                     # student skeleton (5 packages — see src/README.md)
  scaling/               # setup + datasets
  constraints/           # axioms, certificates, guarantee
  search/                # boosting / hard & soft SR paths
  modeling/              # LM architecture + pretraining
  systems/               # HPC profiling + deliverables pipeline
scripts/                 # compile.sh, optional check-latex.sh
Makefile                 # make / make clean / make check
```

## Build (LaTeX)

```bash
bash scripts/compile.sh
# or
make
```

Requires a standard TeX Live / MacTeX install (`pdflatex`, `bibtex`). Use `make clean` to remove aux files. Optionally run `make check` for a from-scratch rebuild that also fails on LaTeX/BibTeX warnings.

## Related

- Scaling-grid checkpoints: [`leibnitz-lab/colinear_scaling_models`](https://huggingface.co/datasets/leibnitz-lab/colinear_scaling_models)
- Method: shape-constrained boosted SR with hard (IA certificates) and soft (violation penalties) paths

## License

[MIT](LICENSE).
