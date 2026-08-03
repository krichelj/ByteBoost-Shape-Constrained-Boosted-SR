# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

LaTeX sources for a ByteBoost 2026 workshop project description (ACCESS cyberinfrastructure testbeds): "Shape-Constrained Boosted Symbolic Regression for Interpretable Neural Scaling Laws." There is no application code — the deliverables are the compiled PDFs, which are committed to the repo.

## Layout

```
documents/
  abstract/       # one-page participant abstract
  description/    # full project description + bibliography
```

## Build commands

```bash
make          # builds documents/description/byteboost_project_description.pdf (pdflatex → bibtex → pdflatex ×2)
make clean    # removes aux files (.aux, .bbl, .blg, .log, .out); keeps PDFs
```

The abstract is NOT covered by the Makefile — build it directly (it has no citations, so no bibtex pass):

```bash
cd documents/abstract && pdflatex -interaction=nonstopmode byteboost_abstract
```

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

## Domain consistency

The requested testbeds are **Neocortex (PSC, Cerebras CS-3)** for pretraining and **AMA27 (Stony Brook, AmpereOne A192-32M Arm cluster)** for the CPU-bound symbolic-regression search. Earlier drafts referenced Ookami/A64FX and CS-2 — those systems were replaced; do not reintroduce them except in the historical note explaining AMA27 replaced the retired Ookami.
