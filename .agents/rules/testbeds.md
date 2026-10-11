# Hardware & Testbed Consistency for ByteBoost 2026

- **Designated Systems**:
  - **Neocortex (PSC)**: Cerebras CS-3 wafer-scale systems for model pretraining.
  - **AMA27 (Stony Brook / ACCESS)**: AmpereOne A192-32M Arm CPU cluster for CPU-bound symbolic regression search.
- **Baselines**:
  - Existing loss baselines are from the public Hugging Face `colinear_scaling_models` collection. Compare *losses*, not original training hardware.
- **Forbidden Hardware**:
  - Do not reference Ookami (A64FX) or Cerebras CS-2 (retired systems).
  - Do not introduce XXXXXXX, GH200, or EPYC as workshop baseline hardware.
- **File Placement**:
  - All experiment runs, profiling benchmarks, and checkpoints must write to dedicated project folders (`runs/<date-slug>/`), never to `$HOME` or temporary paths.
