# Student implementation skeleton

This package is a **formal skeleton** for the ByteBoost project described in
[`documents/description/byteboost_project_description.pdf`](../documents/description/byteboost_project_description.pdf).

Fill in the `NotImplementedError` stubs. Do **not** copy-paste from the
reference submodule; use it to understand algorithms, then implement your own
version.

## Reference implementation

```
reference/axiomatic_neural_scaling_laws/
```

Clone already present as a git submodule (`lab-v2/axiomatic_neural_scaling_laws`).
Study it; implement here.

## Description ↔ skeleton ↔ reference

| Project description | Skeleton package | Reference (study only) |
|---------------------|------------------|------------------------|
| §Setup (`sec:setup`) | `setup/` | `src/data/`, feature maps in boosting |
| §Admissibility axioms A1–A6 (`sec:axioms`) | `axioms/` | `src/constraints/` |
| Stagewise conditions (i)–(vi) (`sec:stage-admiss`) | `axioms/stage_conditions.py` | `docs/methodology.tex`, constraints |
| Interval certificates (`sec:certificates`, eq. interval) | `certificates/` | `src/core/interval.py`, `src/constraints/ia_eval.py` |
| Stage-0 Chinchilla (`sec:boosting`, eq. chinchilla) | `baselines/` | `src/models/baselines.py` |
| Huber \(\delta_j\), \(\tilde r_j\) (eq. delta, pseudoresid) | `residuals/` | `src/core/math_utils.py` |
| Expression trees / \(\mathrm{pow}_p\) | `expression/` | gplearn programs + `ALL_POWERS` |
| Algorithm 1 boosting (`alg:boosting-bb`) | `boosting/` | `src/models/base_boosting.py` |
| Hard path (reject inadmissible \(g\)) | `hard_path/` | *partial* — selection in `axioms_lab.py` |
| Soft path \(v_a\), \(F_j\) (`sec:soft`) | `soft_path/` | `src/constraints/constraints.py`, `fitness.py` |
| Soft search backend (DSO named in description) | `soft_path/backends.py` (`DSOBackend`) | *not in reference* (gplearn used instead) |
| JAX+JVP certificate option (`sec:software`) | `certificates/jax_backend.py` | pure-Python DualInterval in reference |
| Guarantee (`sec:guarantee`) | `guarantee/` | theorems in `docs/methodology.tex` |
| Datasets (`sec:datasets`) | `data/` | `src/data/hf_scaling.py`, … |
| Models (`sec:models`) | `models/` | `src/llm_models/` |
| Pretraining / Neocortex (`sec:testbeds`) | `training/` | `src/training/`, `src/distributed/` |
| AMA27 search profiling (`sec:testbeds`) | `hpc/` | `scripts/tuning/benchmarks/` |
| End-to-end wire-up / deliverables | `pipeline/` | `src/cli.py`, `src/pipeline/` |

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
