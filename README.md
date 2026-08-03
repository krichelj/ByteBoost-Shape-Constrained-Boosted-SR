# ByteBoost 2026

**Shape-Constrained Boosted Symbolic Regression for Interpretable Neural Scaling Laws: A Cross-Testbed Investigation**

Workshop project description for [ByteBoost 2026](https://www.stonybrook.edu/ookami/ByteBoost.php) (ACCESS cyberinfrastructure testbeds). Discover neural scaling-law formulas with symbolic regression, while certifying physical priors (monotonicity, diminishing returns, positivity, irreducible floor, power-law decay) via interval-arithmetic forward-mode AD, across Cerebras CS-3 (Neocortex) pretraining and AmpereOne (AMA27) search.

## Documents

| File | Description |
|------|-------------|
| [`documents/description/byteboost_project_description.pdf`](documents/description/byteboost_project_description.pdf) | Full project description (compiled) |
| [`documents/description/byteboost_project_description.tex`](documents/description/byteboost_project_description.tex) | LaTeX source |
| [`documents/description/byteboost_refs.bib`](documents/description/byteboost_refs.bib) | Bibliography |
| [`documents/abstract/ABSTRACT.md`](documents/abstract/ABSTRACT.md) / [`documents/abstract/byteboost_abstract.tex`](documents/abstract/byteboost_abstract.tex) | Shared participant abstract (Dave Carlson's condensed version) |

## Build

```bash
cd documents/description
pdflatex byteboost_project_description
bibtex   byteboost_project_description
pdflatex byteboost_project_description
pdflatex byteboost_project_description
```

Or from the repo root: `make`.

Requires a standard TeX Live / MacTeX install (`pdflatex`, `bibtex`, and the packages listed in the preamble).

## Build guard

`main` is protected: a from-scratch recompile must produce **no errors and no warnings**, or the change is rejected. CI runs `scripts/check-latex.sh` on every push and PR; enable the same check locally with `git config core.hooksPath githooks`. See [`scripts/README.md`](scripts/README.md).

## Related

- Scaling-grid checkpoints: [`leibnitz-lab/colinear_scaling_models`](https://huggingface.co/datasets/leibnitz-lab/colinear_scaling_models)
- Method: shape-constrained boosted SR with hard (IA certificates) and soft (violation penalties) paths

## License

[MIT](LICENSE).
