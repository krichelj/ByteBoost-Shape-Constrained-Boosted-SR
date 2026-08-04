"""
Primitive operators for symbolic corrections (``sec:boosting``).

Search is over expression trees with operators

    ``{+, −, ×, ÷} ∪ {pow_p : p ∈ P}``

for a finite set ``P ⊂ R ∖ {0}``, where ``pow_p(z) = |z|^p`` for ``z > 0``,
and with bounded depth. Soft ablations may also expose unary ``inv`` / ``log`` /
``sqrt``.

These primitives are ``C^∞`` (hence ``C²`` for A5) only away from the zeros of
their arguments: ``div`` needs a nonzero denominator, and ``pow_p`` a nonzero
argument (``|z|^p`` is unbounded at 0 for ``p < 0`` and not ``C²`` there for the
fractional ``p`` that dominate ``DEFAULT_POWERS``). Interval arithmetic enforces
this on ``I_x`` by returning a non-finite enclosure when an operand straddles 0
(``ia_eval``); beyond ``x_max`` it is a structural side condition
(``stage_conditions``). Note gplearn's stock *protected* division returns 1.0 for
near-zero denominators, which is discontinuous — do not rely on it for A5.

Trees are evaluated on log-features ``log φ_h(h)``; DualInterval certificates on
``I_x ⊂ ℍ̃`` map derivatives back to raw ``N``/``D`` via the chain rule
(``ia_eval``).

Primary backend registration targets gplearn ``make_function``; optional PySR
uses its own operator table.
"""

from __future__ import annotations

from typing import Final, Sequence

# Finite admissible power set P. Replace / extend for your search.
DEFAULT_POWERS: Final[Sequence[float]] = (
    -2.0, -1.0, -0.7, -0.5, -0.3, -0.2, -0.1,
    0.1, 0.2, 0.3, 0.5, 0.7, 2.0, 3.0,
)


def make_power_primitives(powers: Sequence[float] = DEFAULT_POWERS) -> list:
    """Build gplearn ``make_function`` callables for ``pow_p``."""
    raise NotImplementedError("TODO: construct pow_p primitives for gplearn")


def default_function_set() -> list:
    """Return ``{add, sub, mul, div} ∪ {pow_p}`` (optional inv/log/sqrt) for gplearn."""
    raise NotImplementedError("TODO: assemble operator set for tree search")
