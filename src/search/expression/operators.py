"""
Primitive operators for symbolic corrections (``sec:boosting``).

Search is over expression trees with operators

    ``{+, −, ×, ÷} ∪ {pow_p : p ∈ P}``

for a finite set ``P ⊂ R ∖ {0}``, where ``pow_p(z) = |z|^p`` for ``z > 0``,
and with bounded depth. Soft ablations may also expose unary ``inv`` / ``log`` /
``sqrt``.

These primitives are ``C^∞`` on ``(0, ∞)`` (hence ``C²`` for A6). Trees are
evaluated on log-features ``log φ_h(h)``; DualInterval certificates on
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
