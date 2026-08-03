# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

ByteBoost 2026 workshop materials for **Shape-Constrained Boosted Symbolic Regression
for Interpretable Neural Scaling Laws**:

- LaTeX project description / abstract (committed PDFs are deliverables)
- Student implementation skeleton under ``src/`` (formal stubs; students fill in)

There is no private reference implementation in this repository. Students work from
the project description and the ``src/`` stubs only.

## Layout

```
documents/
  abstract/       # one-page participant abstract (.tex, .pdf, ABSTRACT.md)
  description/    # full project description + bibliography
src/              # student skeleton (see src/README.md)
scripts/
  compile.sh      # build PDFs
  check-latex.sh  # optional from-scratch warning-strict check
Makefile          # wraps scripts/compile.sh (+ make check)
```

## Build commands

```bash
bash scripts/compile.sh              # description + abstract PDFs
bash scripts/compile.sh description  # project description only
bash scripts/compile.sh abstract     # participant abstract only
bash scripts/compile.sh clean        # remove aux files; keeps PDFs
```

Or: `make` / `make description` / `make abstract` / `make clean` / `make check`
(wrappers around the scripts). `make check` is an optional from-scratch quality
gate (no errors or warnings).

Requires a standard TeX Live / MacTeX install. After editing a `.tex` file, rebuild and commit the updated PDF alongside the source, since the PDFs are tracked deliverables.

## Document structure and sync invariants

Two documents, one bibliography:

- `documents/description/byteboost_project_description.tex` — the full project description (fields of science, testbed requirements, technical method with theorems/algorithms, deliverables). Uses natbib + cleveref; cites `byteboost_refs.bib` (same directory).
- `documents/abstract/byteboost_abstract.tex` — standalone one-page participant abstract (Dave Carlson's condensed version circulated to ByteBoost 2.0 participants).

**The abstract prose exists in three places that must stay in sync:**
1. `documents/abstract/ABSTRACT.md` (Markdown version, with the metadata table)
2. `documents/abstract/byteboost_abstract.tex`
3. The `\section{Abstract / summary}` of `documents/description/byteboost_project_description.tex` — identical prose, except it adds `\cref{...}` cross-references to later sections

If you edit the abstract wording anywhere, propagate the change to all three (keeping the `\cref` additions only in the project description).

## Student skeleton

See `src/README.md` for the description ↔ package map and suggested implementation order. Keep stub comments aligned with project-description notation (`sec:*`, eq. labels, A1–A6, Algorithm 1). Prefer extending stubs over inventing a parallel layout.

## Domain consistency

The requested testbeds are **Neocortex (PSC, Cerebras CS-3)** for pretraining and **AMA27 (Stony Brook, AmpereOne A192-32M Arm cluster)** for the CPU-bound symbolic-regression search. Earlier drafts referenced Ookami/A64FX and CS-2 — those systems were replaced; do not reintroduce them except in the historical note explaining AMA27 replaced the retired Ookami.
