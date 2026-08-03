# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

ByteBoost 2026 workshop materials for **Shape-Constrained Boosted Symbolic Regression
for Interpretable Neural Scaling Laws**:

- LaTeX project description (committed PDF is a deliverable)
- Student implementation skeleton under ``src/`` (formal stubs; students fill in)

There is no private reference implementation in this repository. Students work from
the project description and the ``src/`` stubs only.

## Layout

```
documents/
  description/    # project description (.tex, .pdf) + bibliography
src/              # student skeleton — five packages (see src/README.md)
  scaling/        # sec:setup, sec:datasets
  constraints/    # sec:axioms, sec:stage-admiss, sec:guarantee
  search/         # sec:boosting, sec:algorithm, sec:soft (+ hard_path extension)
  modeling/       # sec:models, Neocortex pretraining
  systems/        # AMA27/HPC profiling, deliverables pipeline
scripts/
  compile.sh      # build the description PDF
  check-latex.sh  # optional from-scratch warning-strict check
Makefile          # wraps scripts/compile.sh (+ make check)
```

## Build commands

```bash
bash scripts/compile.sh          # project description PDF
bash scripts/compile.sh clean    # remove aux files; keeps PDF
```

Or: `make` / `make clean` / `make check` (wrappers around the scripts).
`make check` is an optional from-scratch quality gate (no errors or warnings).

Requires a standard TeX Live / MacTeX install. After editing the `.tex` file, rebuild and commit the updated PDF alongside the source, since the PDF is a tracked deliverable.

## Document

- `documents/description/byteboost_project_description.tex` — full project description (fields of science, abstract/summary, testbed requirements, technical method with theorems/algorithms, deliverables). Uses natbib + cleveref; cites `byteboost_refs.bib` in the same directory.

## Student skeleton

See `src/README.md` for the description ↔ package map and suggested implementation order. Keep stub comments aligned with project-description notation (`sec:*`, eq. labels, A1–A6, Algorithm 1). Prefer extending stubs over inventing a parallel layout.

## Domain consistency

The requested testbeds are **Neocortex (PSC, Cerebras CS-3)** for pretraining and **AMA27 (Stony Brook, AmpereOne A192-32M Arm cluster)** for the CPU-bound symbolic-regression search. Earlier drafts referenced Ookami/A64FX and CS-2 — those systems were replaced; do not reintroduce them except in the historical note explaining AMA27 replaced the retired Ookami.
