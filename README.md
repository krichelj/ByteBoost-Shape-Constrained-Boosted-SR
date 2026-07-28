# ByteBoost 2026

**Shape-Constrained Boosted Symbolic Regression for Interpretable Neural Scaling Laws: A Cross-Testbed Investigation**

Workshop project description for [ByteBoost 2026](https://www.stonybrook.edu/ookami/ByteBoost.php) (ACCESS cyberinfrastructure testbeds). Discover neural scaling-law formulas with symbolic regression, while certifying physical priors (monotonicity, diminishing returns, positivity, irreducible floor, power-law decay) via interval-arithmetic forward-mode AD—across Cerebras (Neocortex) pretraining and A64FX (Ookami) search.

## Documents

| File | Description |
|------|-------------|
| [`byteboost_project_description.pdf`](byteboost_project_description.pdf) | Full project description (compiled) |
| [`byteboost_project_description.tex`](byteboost_project_description.tex) | LaTeX source |
| [`byteboost_refs.bib`](byteboost_refs.bib) | Bibliography |
| [`byteboost_abstract.tex`](byteboost_abstract.tex) | Short abstract draft |

## Build

```bash
pdflatex byteboost_project_description
bibtex   byteboost_project_description
pdflatex byteboost_project_description
pdflatex byteboost_project_description
```

Or: `make`.

Requires a standard TeX Live / MacTeX install (`pdflatex`, `bibtex`, and the packages listed in the preamble).

## Related

- Scaling-grid checkpoints: [`leibnitz-lab/colinear_scaling_models`](https://huggingface.co/datasets/leibnitz-lab/colinear_scaling_models)
- Method: shape-constrained boosted SR with hard (IA certificates) and soft (violation penalties) paths

## License

[MIT](LICENSE).
