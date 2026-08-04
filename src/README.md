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
| `constraints/` | Admissibility and certificates (`sec:axioms`, `sec:stage-admiss`, `sec:certificates`, `sec:guarantee`) | `axioms/`, `certificates/`, `guarantee/` |
| `search/` | Boosted SR (`sec:boosting`, `sec:algorithm`, `sec:soft`) | `baselines/`, `residuals/`, `expression/`, `soft/` (sole discovery), `boosting/` |
| `modeling/` | Pretraining track (`sec:models`, Neocortex in `sec:testbeds`) | `models/`, `training/` |
| `systems/` | HPC profiling and deliverables (`sec:testbeds` AMA27, `sec:deliverables`) | `hpc/`, `pipeline/` |

## Description ↔ skeleton

Ordered for **implementation**. Soft IA search (``sec:soft``) is the sole
discovery method; Algorithm 1 calls into ``soft/`` at every stage. This
order is close to, but not identical to, the narrative order in §4 of the PDF
(certificates and stage-0 pieces are implemented before the full boosting loop).

| Project description | Skeleton path |
|---------------------|---------------|
| §Setup (`sec:setup`) | `scaling/setup/` (`ℍ`, continuum `ℍ̃`) |
| §Datasets (`sec:datasets`) | `scaling/data/` |
| §Admissibility axioms A1–A5 (`sec:axioms`) | `constraints/axioms/admissibility.py` |
| Stage-0 Chinchilla / NLS (`sec:boosting`, Prop. 1) | `search/baselines/` |
| Huber \(\delta_j\), \(\tilde r_j\) (`sec:boosting`) | `search/residuals/` |
| Expression trees / \(\mathrm{pow}_p\) (`sec:boosting`) | `search/expression/` |
| Stagewise conditions (i)–(vi) (`sec:stage-admiss`, Prop. 2) | `constraints/axioms/stage_conditions.py` |
| DualInterval certificates on \(I_x\subset\widetilde{\mathbb{H}}\) (`sec:certificates`) | `constraints/certificates/` (`interval.py`, `ia_eval.py`, `ia_certificates.py`) |
| Optional JAX+JVP certificate (`sec:software`) | `constraints/certificates/jax_backend.py` |
| Soft search \(v_a\), \(F_j\), gplearn (`sec:soft`, Prop. 3 / zero-penalty ⇒ certificates) | `search/soft/` |
| Soft search backends (gplearn / optional PySR) | `search/soft/backends.py` |
| Algorithm 1 (`sec:algorithm`, `alg:boosting-bb`) | `search/boosting/` |
| Guarantee (`sec:guarantee`, Thm. 1) | `constraints/guarantee/` |
| Existing HF loss / checkpoint baselines (`sec:baselines`) | `scaling/data/scaling_dataset.py` |
| Models (`sec:models`) | `modeling/models/config.py`, `modeling/models/transformer.py` |
| Pretraining / Neocortex (`sec:testbeds`) | `modeling/training/` |
| AMA27 / CPU profiling (`sec:testbeds`) | `systems/hpc/` |
| End-to-end wire-up / deliverables (`sec:deliverables`) | `systems/pipeline/` |
| Collaborator tracks (`sec:collaborators`) | `modeling/` vs `search/` + `systems/hpc/` |

## Suggested implementation order

Dependency order for the soft-only discovery stack. Modeling / systems tracks
are independent of this list.

1. `scaling/` — discrete \(\mathbb{H}\), continuum \(\widetilde{\mathbb{H}}\), \(\mathcal{D}\), `I_x` domains
2. `constraints/certificates/interval.py` — `Interval`, `DualInterval` (incl. `d2` for A2)
3. `constraints/axioms/admissibility.py` — A1–A5 on \(\widetilde{\mathbb{H}}\)
4. `search/baselines/` — NLS admissible \(\widehat L_0\)
5. `search/residuals/` — Huber stage targets
6. `search/expression/` + `constraints/certificates/ia_eval.py` — trees, \(\mathrm{ord}\), log→raw
7. `constraints/axioms/stage_conditions.py` + certificate enclosures on \(I_x\subset\widetilde{\mathbb{H}}\)
8. `search/soft/` — gplearn + IA penalties (A5 via DualInterval finiteness / ``C^∞``)
9. `search/boosting/` — Algorithm 1 (`sec:algorithm`)
10. `constraints/guarantee/` — floor / exponent checks on \(\widetilde{\mathbb{H}}\)
11. Modeling / systems tracks as assigned: `modeling/`, `systems/hpc/`

## Notation

Symbols match Appendix A of the project description (`N`, `D`, \(\mathcal{H}\),
\(\mathbb{H}\), \(\widetilde{\mathbb{H}}\), \(\widehat L\), \(\mathcal{S}\),
\(L_\infty\), \(c_x^{(0)}\), …). Prefer those names in identifiers and comments.
