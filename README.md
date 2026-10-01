# ByteBoost 2026

**Shape-Constrained Boosted Symbolic Regression for Interpretable Neural Scaling Laws: A Cross-Testbed Investigation**

Workshop project for [ByteBoost 2026](https://www.stonybrook.edu/ookami/ByteBoost.php) (ACCESS cyberinfrastructure testbeds; URL path is historical). Discover neural scaling-law formulas with symbolic regression, while certifying physical priors (A1–A5: monotonicity, diminishing returns, irreducible floor, power-law decay, graceful saturation) via interval-arithmetic forward-mode AD, across Cerebras CS-3 (Neocortex) pretraining and AmpereOne (AMA27) search.

## Documents

- [Project description](documents/description/byteboost_project_description.pdf)
- [HPC allocation abstract](documents/abstract/byteboost_abstract.pdf)

## Student skeleton

Implement the method in [`src/`](src/), organized into five packages (`scaling`, `constraints`, `search`, `modeling`, `systems`). Stubs use the description’s notation and raise `NotImplementedError`; see [`src/README.md`](src/README.md) for the full map and suggested order.

Run Python from the repository root so imports like `from src.scaling.setup…` resolve.

## Repository layout

```
documents/description/   # LaTeX source, bibliography, committed PDF (history/: older copies)
documents/abstract/      # one-page HPC allocation abstract
src/                     # student skeleton (5 packages, see src/README.md)
  scaling/               # setup + datasets
  constraints/           # axioms, certificates, guarantee
  search/                # stage-0 / residuals / soft SR (sole) / Algorithm 1
  modeling/              # LM architecture + pretraining
  systems/               # HPC profiling + deliverables pipeline
tests/                   # falsifiable tests mirroring component structure
  constraints/           # interval arithmetic and certificate tests
  scaling/               # constants and domain configuration tests
  scripts/               # build script and deliverable integrity tests
  search/                # operator set and tree tests
scripts/                 # compile.sh, check-latex.sh
.github/workflows/       # GitHub Actions CI quality gates
.agents/rules/           # Antigravity IDE workspace rules
Makefile                 # make (pdf) / make check (LaTeX + Python suite)
pyproject.toml           # uv project definitions and dependency groups
ruff.toml                # pinned Ruff lint and format configurations
AGENTS.md                # operational rules for AI coding assistants
```

## Setup and environment

Python dependencies and virtual environments are managed strictly with [`uv`](https://docs.astral.sh/uv/):

```bash
uv sync --all-groups
```

## Quality gates and testing

Run the full unified quality gate (LaTeX checks, Ruff lint/format, Mypy type-checking, and Pytest suite):

```bash
make check
```

Individual component gates:

```bash
make test         # or: uv run pytest -v
make lint         # or: uv run ruff check . && uv run ruff format --check .
make types        # or: uv run mypy src/ tests/
make check-latex  # or: bash scripts/check-latex.sh
```

Pre-commit hooks are wired with `pre-commit`:

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

## Build (LaTeX)

```bash
bash scripts/compile.sh
# or
make
```

Requires a standard TeX Live / MacTeX install (`pdflatex`, `bibtex`, `latexmk`). Use `make clean` to remove aux files.

## Related

- Public HF loss / checkpoint baselines (`sec:baselines`): [`leibnitz-lab/colinear_scaling_models`](https://huggingface.co/datasets/leibnitz-lab/colinear_scaling_models); compare *losses*, not original training hardware
- Method: shape-constrained boosted SR with soft IA violation penalties in the GP fitness

## License

[MIT](LICENSE).
