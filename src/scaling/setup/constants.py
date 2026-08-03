"""
Global symbols aligned with project-description §Notation / ``sec:setup``.

Students may extend this module with experiment-specific constants
(e.g. concrete grids ``H_N``, ``H_D``) without changing the formal meaning
of the symbols below.
"""

from __future__ import annotations

from typing import Final

# Scale variables x ∈ {N, D} (parameter count and training-token count).
SCALE_VARS: Final[tuple[str, str]] = ("N", "D")

# Tokens-per-parameter ratio M = D/N (``sec:models``).
# Concrete grids are experiment-specific; define them when loading data.
# M_GRID: Sequence[float] = ...

# Soft-path axiom indices a ∈ {mono, conv, irred, decay, leaf}
# (``sec:soft``, eq. violations-bb). Positivity (A5) and graceful saturation (A6)
# are certified via the irreducible-floor / finiteness IA checks rather than
# separate soft scores (see project description).
AXIOM_INDICES: Final[tuple[str, ...]] = (
    "mono",
    "conv",
    "irred",
    "decay",
    "leaf",
)

# Positive margin ε_decay in v_decay so that a zero score implies the strict
# power-law inequality required by stage condition (v).
EPSILON_DECAY: Final[float] = 0.05

# Placeholder penalty weights λ_a > 0. Tune on your data; defaults are illustrative.
DEFAULT_LAMBDAS: Final[dict[str, float]] = {
    "mono": 10.0,
    "conv": 5.0,
    "irred": 20.0,
    "decay": 5.0,
    "leaf": 15.0,
}
