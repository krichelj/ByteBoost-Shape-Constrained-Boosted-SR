.PHONY: all description pdf clean check-latex lint format types test check

SHELL := /bin/bash

all description pdf:
	bash scripts/compile.sh description

clean:
	bash scripts/compile.sh clean

# From-scratch LaTeX quality gate (0 errors, 0 warnings, 0 overfull boxes).
check-latex:
	bash scripts/check-latex.sh

# Python quality gates
lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check --fix .
	uv run ruff format .

types:
	uv run mypy src/ tests/

test:
	uv run pytest -v

# Run all quality gates (LaTeX + Python)
check: check-latex lint types test
