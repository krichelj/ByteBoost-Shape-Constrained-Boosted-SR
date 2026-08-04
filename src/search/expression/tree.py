"""
Expression-tree abstraction for a candidate correction ``g`` (``sec:boosting``).

The project description treats ``g`` as a finite expression tree over
``{+, −, ×, ÷} ∪ {pow_p}`` (and optional unary ablations). Those primitives are
``C^∞`` away from the zeros of their arguments, so a finite ``F̄ < ∞`` enclosure
(which also certifies that no denominator or ``pow_p`` argument vanished)
discharges graceful saturation (A5) on certification boxes; see ``operators.py``
for the domain caveat. Concrete encodings (gplearn prefix lists,
sympy, PySR expressions, …) are left to students; this protocol captures the
operations DualInterval certificates on ``I_x ⊂ ℍ̃`` and soft scores need.
"""

from __future__ import annotations

from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class ExpressionTree(Protocol):
    """Minimal surface used by IA evaluation and structural checks."""

    def as_program(self) -> Any:
        """Backend-native program encoding."""
        ...

    def feature_indices(self) -> list[int]:
        """Global feature indices referenced by this tree."""
        ...

    def __str__(self) -> str:
        """Readable formula for deliverables / logs."""
        ...
