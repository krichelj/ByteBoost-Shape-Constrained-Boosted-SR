"""
Primitive operators for symbolic corrections (``sec:boosting``).

Search is over expression trees with operators

    ``{+, ×, ÷} ∪ {pow_p : p ∈ P}``

for a finite set ``P ⊂ R ∖ {0}``, where ``pow_p(z) = |z|^p`` for ``z > 0``,
and with bounded depth.

Students choose how to register these with gplearn / DSO / a custom engine.
"""

from __future__ import annotations

from typing import Final, Sequence

# Finite admissible power set P. Replace / extend for your search.
DEFAULT_POWERS: Final[Sequence[float]] = (
    -2.0, -1.0, -0.7, -0.5, -0.3, -0.2, -0.1,
    0.1, 0.2, 0.3, 0.5, 0.7, 2.0, 3.0,
)


def make_power_primitives(powers: Sequence[float] = DEFAULT_POWERS) -> list:
    """Build library callables / gplearn ``make_function`` objects for ``pow_p``.

    Return type depends on the chosen SR backend.
    """
    raise NotImplementedError("TODO: construct pow_p primitives for your SR library")


def default_function_set() -> list:
    """Return ``{add, mul, div, …} ∪ {pow_p}`` suitable for the chosen backend."""
    raise NotImplementedError("TODO: assemble operator set for tree search")
