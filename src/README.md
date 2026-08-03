# Student implementation skeleton

This package is a **formal skeleton** for the ByteBoost project described in
[`documents/description/byteboost_project_description.pdf`](../documents/description/byteboost_project_description.pdf).

Fill in the `NotImplementedError` stubs. Use the project description’s notation
and equations; concrete dtypes, backends, and grids are yours to choose.

Work from the repository root so package imports resolve, e.g.
`from src.scaling.setup.configuration import ConfigurationSpace`.

## Top-level layout (5 packages)

| Package | Role | Subpackages |
|---------|------|-------------|
| `scaling/` | Problem setup and data (`sec:setup`, `sec:datasets`, notation) | `setup/`, `data/` |
| `constraints/` | Admissibility and certificates (`sec:axioms`, `sec:certificates`, `sec:guarantee`) | `axioms/`, `certificates/`, `guarantee/` |
| `search/` | Shape-constrained SR / Algorithm 1 (`sec:boosting`, `sec:soft`) | `baselines/`, `residuals/`, `expression/`, `boosting/`, `hard_path/`, `soft_path/` |
| `modeling/` | Pretraining track (`sec:models`, Neocortex in `sec:testbeds`) | `models/`, `training/` |
| `systems/` | HPC profiling and deliverables (`sec:testbeds` AMA27, `sec:deliverables`) | `hpc/`, `pipeline/` |

## Description ↔ skeleton

| Project description | Skeleton path |
|---------------------|---------------|
| §Setup (`sec:setup`) | `scaling/setup/` |
| §Datasets (`sec:datasets`) | `scaling/data/` |
| §Admissibility axioms A1–A6 (`sec:axioms`) | `constraints/axioms/` |
| Stagewise conditions (i)–(vi) (`sec:stage-admiss`) | `constraints/axioms/stage_conditions.py` |
| Interval certificates (`sec:certificates`, eq. interval) | `constraints/certificates/` |
| JAX+JVP certificate option (`sec:software`) | `constraints/certificates/jax_backend.py` |
| Guarantee (`sec:guarantee`) | `constraints/guarantee/` |
| Stage-0 Chinchilla (`sec:boosting`, eq. chinchilla) | `search/baselines/` |
| Huber \(\delta_j\), \(\tilde r_j\) | `search/residuals/` |
| Expression trees / \(\mathrm{pow}_p\) | `search/expression/` |
| Algorithm 1 (`alg:boosting-bb`) | `search/boosting/` |
| Hard path (reject inadmissible \(g\)) | `search/hard_path/` |
| Soft path \(v_a\), \(F_j\) (`sec:soft`) | `search/soft_path/` |
| Soft search backends (gplearn / DSO) | `search/soft_path/backends.py` |
| Models (`sec:models`) | `modeling/models/` |
| Pretraining / Neocortex (`sec:testbeds`) | `modeling/training/` |
| AMA27 / hardware profiling (`sec:testbeds`, `sec:baselines`) | `systems/hpc/` |
| End-to-end wire-up / deliverables | `systems/pipeline/` |
| Software stack notes (`sec:software`) | comments in `search/soft_path/`, `constraints/certificates/jax_backend.py`, `modeling/training/` |
| Collaborator tracks (`sec:collaborators`) | `modeling/` vs `search/` + `systems/hpc/` |

## Suggested implementation order

1. `scaling/` — configuration space \(\mathbb{H}\) and dataset \(\mathcal{D}\)
2. `constraints/certificates/interval.py` — `Interval`, `DualInterval`
3. `search/baselines/` — admissible \(\widehat L_0\)
4. `search/residuals/` — Huber stage targets
5. `search/expression/` + `constraints/certificates/ia_eval.py` — trees, \(\mathrm{ord}(g,x)\)
6. `constraints/axioms/` + hard certificates — A1–A6 / (i)–(vi)
7. `search/hard_path/` then `search/soft_path/` — two search methods
8. `search/boosting/` — Algorithm 1
9. `constraints/guarantee/` — floor / exponent checks
10. Modeling / systems tracks as assigned: `modeling/`, `systems/hpc/`

## Notation

Symbols match §Notation of the project description (`N`, `D`, \(\mathcal{H}\),
\(\widehat L\), \(\mathcal{S}\), \(L_\infty\), \(c_x^{(0)}\), …). Prefer those
names in identifiers and comments.
