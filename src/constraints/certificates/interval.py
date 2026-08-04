"""
Interval arithmetic and forward-mode AD duals (``sec:certificates``).

Sound enclosures ``f̲ ≤ f ≤ f̄`` on a compact box ``I_x = [x_min, x_max]``
(``I_x`` ≡ ``ℐ_x`` / ``\\calI_x`` in the project description) are the substrate
for continuum certificates on a slice of ``ℍ̃`` (``sec:setup``, ``sec:axioms``):

* (A1)/(i)  via ``∂F/∂x̄ ≤ 0``
* (A2)/(ii) via ``∂²F/∂x²̲ ≥ 0``  (needs the second-derivative dual)
* (A3)/(iv) via ``F̲ > L_∞`` (``L_∞ > 0`` ⇒ ensemble positivity / stage (iii))
* (A5)/(vi) via ``F̄ < ∞`` plus the ``C²`` (in practice ``C^∞``) operator set

The half-line ``x > x_max`` is *not* covered by ``I_x``; structural ``ord``
handles that tail (certificate (b)). Composition with forward-mode AD yields
enclosures of ``F``, ``∂F/∂x``, and ``∂²F/∂x²`` in time linear in the
expression-tree size.

Soft search (``sec:soft``) converts these enclosures into continuous ``v_a``
scores that enter the fitness.
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

    def __radd__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: reverse interval addition")

    def __sub__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: interval subtraction")

    def __rsub__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: reverse interval subtraction")

    def __mul__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: interval multiplication")

    def __rmul__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: reverse interval multiplication")

    def __truediv__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: interval division (handle 0 ∈ divisor)")

    def __rtruediv__(self, other: Interval | Scalar) -> Interval:
        raise NotImplementedError("TODO: reverse interval division")

    def __neg__(self) -> Interval:
        raise NotImplementedError("TODO: interval negation")

    @staticmethod
    def power(base: Interval, exp: float) -> Interval:
        """Enclosure of ``z ↦ |z|^p`` style powers used by ``pow_p``."""
        raise NotImplementedError("TODO: power enclosure for positive bases")


@dataclass
class DualInterval:
    """Forward-mode AD value: ``(val, d1, d2)`` as intervals.

    Carries the value and the first two derivatives w.r.t. one differentiated
    scale coordinate ``x`` on the certification box ``I_x ⊂ ℍ̃``. For that
    coordinate use ``variable(domain)``; for other coordinates held fixed, use
    ``parameter(domain)``.

    Arithmetic must propagate derivative rules (product, quotient, chain rule
    for ``pow_p``) so tree evaluation yields sound enclosures of
    ``F``, ``∂F/∂x``, ``∂²F/∂x²`` on ``I_x`` (eq. interval-bb). The second
    derivative dual is required for diminishing-returns / (A2).
    """

    val: Interval
    d1: Interval
    d2: Interval

    @staticmethod
    def constant(c: float) -> DualInterval:
        """Constant leaf: value ``[c,c]``, derivatives zero."""
        raise NotImplementedError("TODO: DualInterval with zero derivatives")

    @staticmethod
    def variable(domain: Interval) -> DualInterval:
        """Independent variable on ``domain`` (``d1 = [1,1]``, ``d2 = [0,0]``)."""
        raise NotImplementedError("TODO: DualInterval.variable")

    @staticmethod
    def parameter(domain: Interval) -> DualInterval:
        """Frozen coordinate (derivatives zero)."""
        raise NotImplementedError("TODO: DualInterval.parameter")

    # --- DualInterval arithmetic (same operator set as Interval / trees) ---

    def __add__(self, other: DualInterval | Scalar) -> DualInterval:
        raise NotImplementedError("TODO: dual addition (val, d1, d2)")

    def __radd__(self, other: DualInterval | Scalar) -> DualInterval:
        raise NotImplementedError("TODO: reverse dual addition")

    def __sub__(self, other: DualInterval | Scalar) -> DualInterval:
        raise NotImplementedError("TODO: dual subtraction")

    def __rsub__(self, other: DualInterval | Scalar) -> DualInterval:
        raise NotImplementedError("TODO: reverse dual subtraction")

    def __mul__(self, other: DualInterval | Scalar) -> DualInterval:
        raise NotImplementedError("TODO: dual product rule")

    def __rmul__(self, other: DualInterval | Scalar) -> DualInterval:
        raise NotImplementedError("TODO: reverse dual product")

    def __truediv__(self, other: DualInterval | Scalar) -> DualInterval:
        raise NotImplementedError("TODO: dual quotient rule (0 ∉ divisor)")

    def __rtruediv__(self, other: DualInterval | Scalar) -> DualInterval:
        raise NotImplementedError("TODO: reverse dual quotient")

    def __neg__(self) -> DualInterval:
        raise NotImplementedError("TODO: dual negation")

    @staticmethod
    def power(base: DualInterval, exp: float) -> DualInterval:
        """Dual enclosure of ``pow_p(z) = |z|^p`` (chain rule on val/d1/d2)."""
        raise NotImplementedError("TODO: dual power for pow_p")
