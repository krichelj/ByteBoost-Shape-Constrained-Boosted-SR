"""Tests verifying project build scripts and deliverable integrity."""

from __future__ import annotations

import os
from pathlib import Path


def test_build_scripts_executable(repo_root: Path) -> None:
    """Scripts in scripts/ must be present and marked executable."""
    scripts = [
        repo_root / "scripts" / "compile.sh",
        repo_root / "scripts" / "check-latex.sh",
    ]
    for s in scripts:
        assert s.is_file(), f"Missing script: {s}"
        assert os.access(s, os.X_OK), f"Script not executable: {s}"


def test_tracked_deliverables_exist(repo_root: Path, description_dir: Path) -> None:
    """Project description PDF and LaTeX sources must be committed deliverables."""
    assert (description_dir / "byteboost_project_description.tex").is_file()
    assert (description_dir / "byteboost_refs.bib").is_file()
    pdf = description_dir / "byteboost_project_description.pdf"
    assert pdf.is_file(), "Committed deliverable PDF is missing"
    assert pdf.stat().st_size > 50_000, "PDF file is suspiciously small or empty"


def test_citation_metadata_author(repo_root: Path) -> None:
    """CITATION.cff must record the author's full formal name."""
    cff_path = repo_root / "CITATION.cff"
    assert cff_path.is_file(), "CITATION.cff must exist at repository root"
    content = cff_path.read_text(encoding="utf-8")
    assert "family-names: Kricheli" in content
    assert "given-names: Joshua Shay" in content
