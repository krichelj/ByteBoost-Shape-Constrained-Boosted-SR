"""
Interval arithmetic and forward-mode AD duals (``sec:certificates``).

Sound enclosures ``f̲ ≤ f ≤ f̄`` on a compact box ``I_x = [x_min, x_max]`` are
the substrate for continuum certificates of (A1)–(A4)/(A6) and stage
conditions (i)–(iv), (vi). Composition with forward-mode AD yields enclosures
of ``F``, ``∂F/∂x``, and ``∂²F/∂x²`` in time linear in the expression-tree size.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Union

Scalar = Union[int, float]


@dataclass
class Interval:
    """Closed interval ``[lo, hi]`` with rigorous arithmetic."""

    lo: float
    hi: float

    def __post_init__(self) -> None:
        raise NotImplementedError("TODO: validate lo ≤ hi; reject NaN bounds")

    # --- arithmetic (implement all used by tree evaluation) ---

    def __add__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: interval addition")

    def __sub__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: interval subtraction")

    def __mul__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: interval multiplication")

    def __truediv__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: interval division (handle 0 ∈ divisor)")

    @staticmethod
    def power(base: Interval, exp: float) -> Interval:
        """Enclosure of ``z ↦ |z|^p`` style powers used by ``pow_p``."""
        raise NotImplementedError("TODO: power enclosure for positive bases")


@dataclass
class DualInterval:
    """Forward-mode AD value: ``(val, d1, d2)`` as intervals.

    For the differentiated coordinate ``x``, use ``variable(domain)``;
    for other coordinates held fixed, use ``parameter(domain)``.
    """

    val: Interval
    d1: Interval
    d2: Interval

    @staticmethod
    def constant(c: float) -> DualInterval:
        raise NotImplementedError("TODO: DualInterval with zero derivatives")

    @staticmethod
    def variable(domain: Interval) -> DualInterval:
        """Independent variable on ``domain`` (``d1 = [1,1]``, ``d2 = [0,0]``)."""
        raise NotImplementedError("TODO: DualInterval.variable")

    @staticmethod
    def parameter(domain: Interval) -> DualInterval:
        """Frozen coordinate (derivatives zero)."""
        raise NotImplementedError("TODO: DualInterval.parameter")
