"""
Expression-tree abstraction for a candidate correction ``g`` (``sec:boosting``).

The project description treats ``g`` as a finite expression tree over
``{+, −, ×, ÷} ∪ {pow_p}`` (and optional unary ablations). Concrete encodings
(gplearn prefix lists, sympy, PySR expressions, …) are left to students; this
protocol captures the operations DualInterval certificates and soft scores need.
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
