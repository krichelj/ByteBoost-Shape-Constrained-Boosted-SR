"""
Global symbols aligned with project-description §Notation / ``sec:setup``.

Includes scale names, soft-path axiom indices, and illustrative ``λ_a`` /
``ε_decay``. Continuum domain ``ℍ̃`` and certification boxes ``I_x`` are
constructed from the configuration space (``configuration.py``), not stored
as globals here.

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
# (``sec:soft``, eq. violations-bb). Positivity (A5) is implied by the joint
# floor when L_∞ > 0 and is folded into v_irred; graceful saturation (A6) is
# certified via DualInterval finiteness / the C² (in practice C^∞) operator set
# rather than a separate soft score — prop:soft requires V=0 *and* finite
# enclosures (see project description ``sec:axioms``, ``sec:soft``).
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
