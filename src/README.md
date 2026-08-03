# Student implementation skeleton

This package is a **formal skeleton** for the ByteBoost project described in
[`documents/description/byteboost_project_description.pdf`](../documents/description/byteboost_project_description.pdf).

Fill in the `NotImplementedError` stubs. Use the project description’s notation
and equations; concrete dtypes, backends, and grids are yours to choose.

Work from the repository root so package imports resolve, e.g.
`from src.setup.configuration import ConfigurationSpace`.

## Description ↔ skeleton

| Project description | Skeleton package |
|---------------------|------------------|
| §Setup (`sec:setup`) | `setup/` |
| §Admissibility axioms A1–A6 (`sec:axioms`) | `axioms/` |
| Stagewise conditions (i)–(vi) (`sec:stage-admiss`) | `axioms/stage_conditions.py` |
| Interval certificates (`sec:certificates`, eq. interval) | `certificates/` |
| Stage-0 Chinchilla (`sec:boosting`, eq. chinchilla) | `baselines/` |
| Huber \(\delta_j\), \(\tilde r_j\) (eq. delta, pseudoresid) | `residuals/` |
| Expression trees / \(\mathrm{pow}_p\) | `expression/` |
| Algorithm 1 boosting (`alg:boosting-bb`) | `boosting/` |
| Hard path (reject inadmissible \(g\)) | `hard_path/` |
| Soft path \(v_a\), \(F_j\) (`sec:soft`) | `soft_path/` |
| Soft search backends (gplearn / DSO) | `soft_path/backends.py` |
| JAX+JVP certificate option (`sec:software`) | `certificates/jax_backend.py` |
| Guarantee (`sec:guarantee`) | `guarantee/` |
| Datasets (`sec:datasets`) | `data/` |
| Models (`sec:models`) | `models/` |
| Pretraining / Neocortex (`sec:testbeds`) | `training/` |
| AMA27 search profiling (`sec:testbeds`) | `hpc/` |
| End-to-end wire-up / deliverables | `pipeline/` |

## Suggested implementation order

1. `setup/` + `data/` — configuration space \(\mathbb{H}\) and dataset \(\mathcal{D}\)
2. `certificates/interval.py` — `Interval`, `DualInterval`
3. `baselines/` — admissible \(\widehat L_0\)
4. `residuals/` — Huber stage targets
5. `expression/` + `certificates/ia_eval.py` — trees, \(\mathrm{ord}(g,x)\), leaves
6. `axioms/` + `certificates/hard_certificates.py` — A1–A6 / (i)–(vi)
7. `hard_path/` then `soft_path/` — two search methods
8. `boosting/` — Algorithm 1
9. `guarantee/` — floor / exponent checks
10. Modeling track: `models/`, `training/`, `hpc/` as assigned

## Notation

Symbols match §Notation of the project description (`N`, `D`, \(\mathcal{H}\),
\(\widehat L\), \(\mathcal{S}\), \(L_\infty\), \(c_x^{(0)}\), …). Prefer those
names in identifiers and comments.
