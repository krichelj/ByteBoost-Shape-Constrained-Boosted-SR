"""Shared pytest configuration and fixtures for ByteBoost 2026."""

from __future__ import annotations

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture
def repo_root() -> Path:
    """Return the absolute path to the repository root."""
    return REPO_ROOT


@pytest.fixture
def description_dir(repo_root: Path) -> Path:
    """Return the directory containing project description LaTeX sources."""
    return repo_root / "documents" / "description"
