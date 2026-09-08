# AGENTS.md

Guidance for AI agents working in the ByteBoost 2026 repository.

## Operational Rules

1. **Python Environment**: Always use `uv` (`uv sync`, `uv run`, `uv add`). Never use bare pip, poetry, or conda.
2. **Quality Gates**:
   - Python linting: `uv run ruff check . && uv run ruff format --check .`
   - Static typing: `uv run mypy src/ tests/`
   - Tests: `uv run pytest -v`
   - LaTeX: `bash scripts/check-latex.sh` (0 errors, 0 warnings, 0 overfull boxes)
   - Pre-commit: `uv run pre-commit run --all-files`
3. **Proof Discipline**: Every feature and claim must have a formal, falsifiable test in `tests/` with negative controls.
4. **LaTeX & Proof Writing**:
   - Introduce objects with `Let` or `Define` (never `Fix`, `Put`, `Set`, `Write`, `Take`).
   - Bidirectional proofs: `\textbf{($\Longrightarrow$)}` first, `\textbf{($\Longleftarrow$)}` second.
   - Number only displays that are cited.
   - Strike archaic AI vocabulary (`whence`, `moreover`, `delve`, `tapestry`, etc.).
5. **Author & Git Identity**:
   - Author: **Joshua Shay Kricheli**
   - Git Email: `skricheli2@gmail.com`
   - Remote: Personal repository (`git@github.com:krichelj/ByteBoost-Shape-Constrained-Boosted-SR.git`)
6. **Hardware Testbeds**:
   - Neocortex (Cerebras CS-3) for pretraining; AMA27 (AmpereOne A192-32M) for symbolic regression search.
   - Compare losses against Hugging Face `colinear_scaling_models`.
