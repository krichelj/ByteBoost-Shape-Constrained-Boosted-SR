# ByteBoost 2026

**Shape-Constrained Boosted Symbolic Regression for Interpretable Neural Scaling Laws: A Cross-Testbed Investigation**

Workshop project for [ByteBoost 2026](https://www.stonybrook.edu/ookami/ByteBoost.php) (ACCESS cyberinfrastructure testbeds). Discover neural scaling-law formulas with symbolic regression, while certifying physical priors (monotonicity, diminishing returns, positivity, irreducible floor, power-law decay) via interval-arithmetic forward-mode AD, across Cerebras CS-3 (Neocortex) pretraining and AmpereOne (AMA27) search.

## Documents

- [Project description](documents/description/byteboost_project_description.pdf)

## Student skeleton

Implement the method in [`src/`](src/). Each subpackage maps to a section of the project description (setup, axioms, certificates, boosting, hard/soft paths, modeling track, …). Stubs use the description’s notation and raise `NotImplementedError` — see [`src/README.md`](src/README.md) for the full map and suggested order.

## Build (LaTeX)

```bash
bash scripts/compile.sh
# or
make
```

Requires a standard TeX Live / MacTeX install (`pdflatex`, `bibtex`). Pass `description`, `abstract`, or `clean` to compile one document or remove aux files (`make` accepts the same targets). Optionally run `make check` for a from-scratch rebuild that also fails on LaTeX/BibTeX warnings.

## Related

- Scaling-grid checkpoints: [`leibnitz-lab/colinear_scaling_models`](https://huggingface.co/datasets/leibnitz-lab/colinear_scaling_models)
- Method: shape-constrained boosted SR with hard (IA certificates) and soft (violation penalties) paths

## License

[MIT](LICENSE).
