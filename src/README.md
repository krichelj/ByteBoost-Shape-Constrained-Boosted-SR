# Student implementation skeleton

This package is a **formal skeleton** for the ByteBoost project described in
[`documents/description/byteboost_project_description.pdf`](../documents/description/byteboost_project_description.pdf).

Fill in the `NotImplementedError` stubs. Use the project description’s notation
(Appendix A) and equations; concrete dtypes, backends, and grids are yours to
choose. The description ↔ package map is Appendix B of the PDF (and below).
Formal proofs are Appendix C.

Work from the repository root so package imports resolve, e.g.
`from src.scaling.setup.configuration import ConfigurationSpace`.

## Top-level layout (5 packages)

| Package | Role | Subpackages |
|---------|------|-------------|
| `scaling/` | Problem setup and data (`sec:setup`, `sec:datasets`) | `setup/`, `data/` |
| `constraints/` | Admissibility and certificates (`sec:axioms`, `sec:stage-admiss`, `sec:guarantee`) | `axioms/`, `certificates/`, `guarantee/` |
| `search/` | Boosted SR (`sec:boosting`, `sec:algorithm`, `sec:soft`) | `baselines/`, `residuals/`, `expression/`, `soft_path/`, `hard_path/`, `boosting/` |
| `modeling/` | Pretraining track (`sec:models`, Neocortex in `sec:testbeds`) | `models/`, `training/` |
| `systems/` | HPC profiling and deliverables (`sec:testbeds` AMA27, `sec:deliverables`) | `hpc/`, `pipeline/` |

## Description ↔ skeleton

Ordered for **implementation** (soft primary before optional hard filter), not
strict §4 narrative order. Soft appears before Algorithm 1 because Algorithm 1
calls into the search backends.

| Project description | Skeleton path |
|---------------------|---------------|
| §Setup (`sec:setup`) | `scaling/setup/` |
| §Datasets (`sec:datasets`) | `scaling/data/` |
| §Admissibility axioms A1–A6 (`sec:axioms`) | `constraints/axioms/admissibility.py` |
| Stage-0 Chinchilla / NLS (`sec:boosting`, Prop. 1) | `search/baselines/` |
| Huber \(\delta_j\), \(\tilde r_j\) (`sec:boosting`) | `search/residuals/` |
| Expression trees / \(\mathrm{pow}_p\) (`sec:boosting`) | `search/expression/` |
| Stagewise conditions (i)–(vi) (`sec:stage-admiss`, Prop. 2) | `constraints/axioms/stage_conditions.py` |
| DualInterval certificates (`sec:certificates`) | `constraints/certificates/` (`interval.py`, `ia_eval.py`, `hard_certificates.py`) |
| Optional JAX+JVP certificate (`sec:software`) | `constraints/certificates/jax_backend.py` |
| Soft path \(v_a\), \(F_j\), gplearn (`sec:soft`, Prop. 3) | `search/soft_path/` |
| Soft search backends (gplearn / optional PySR) | `search/soft_path/backends.py` |
| Hard path / reject filter (`sec:stage-admiss`, workshop) | `search/hard_path/` |
| Algorithm 1 (`sec:algorithm`, `alg:boosting-bb`) | `search/boosting/` |
| Guarantee (`sec:guarantee`, Thm. 1) | `constraints/guarantee/` |
| Models (`sec:models`) | `modeling/models/config.py`, `modeling/models/transformer.py` |
| Pretraining / Neocortex (`sec:testbeds`) | `modeling/training/` |
| AMA27 / CPU profiling (`sec:testbeds`, `sec:baselines`) | `systems/hpc/` |
| End-to-end wire-up / deliverables (`sec:deliverables`) | `systems/pipeline/` |
| Collaborator tracks (`sec:collaborators`) | `modeling/` vs `search/` + `systems/hpc/` |

## Suggested implementation order

Dependency order (soft search is primary; hard filter is optional workshop
extension). This is *not* the same as §4 section order in the PDF.

1. `scaling/` — \(\mathbb{H}\) and \(\mathcal{D}\)
2. `constraints/certificates/interval.py` — `Interval`, `DualInterval`
3. `constraints/axioms/admissibility.py` — A1–A6
4. `search/baselines/` — NLS admissible \(\widehat L_0\)
5. `search/residuals/` — Huber stage targets
6. `search/expression/` + `constraints/certificates/ia_eval.py` — trees, \(\mathrm{ord}\), log→raw
7. `constraints/axioms/stage_conditions.py` + certificate enclosures
8. `search/soft_path/` — primary gplearn + IA penalties
9. `search/hard_path/` — optional reject filter (workshop extension)
10. `search/boosting/` — Algorithm 1 (`sec:algorithm`)
11. `constraints/guarantee/` — floor / exponent checks
12. Modeling / systems tracks as assigned: `modeling/`, `systems/hpc/`

## Notation

Symbols match Appendix A of the project description (`N`, `D`, \(\mathcal{H}\),
\(\widehat L\), \(\mathcal{S}\), \(L_\infty\), \(c_x^{(0)}\), …). Prefer those
names in identifiers and comments.
