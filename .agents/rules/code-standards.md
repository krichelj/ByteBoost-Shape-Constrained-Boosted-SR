# Python & Engineering Standards for ByteBoost 2026

- **Virtual Environments & Dependencies**: Always use `uv` (`uv sync`, `uv run`, `uv add`). Never use bare pip, poetry, or conda.
- **Linting & Formatting**: Enforce `ruff check` and `ruff format` using project `ruff.toml`. Enforce `shfmt -i 2 -ci -w` and `shellcheck` for shell scripts.
- **Static Typing**: Use Python 3.10+ PEP 585 built-in collections (`list`, `dict`, `set`, `tuple`, `collections.abc.Sequence`, `collections.abc.Mapping`) and PEP 604 union syntax (`int | float`, `X | None`). All code must pass `mypy` with project floor flags.
- **Proof Rule**: Every claim and functional component must be verified with formal, falsifiable tests in `tests/`. Tests must prove non-trivial behavior with negative controls.
- **Filesystem Policy**: Never create symlinks. Always use real files.
