"""
Sound interval certificates on the compact box ``I_x`` (``sec:certificates``,
eq. interval-bb).

Let ``F = L̂^{(j−1)} + g``. Forward-mode AD + IA returns enclosures of
``F``, ``∂F/∂x``, ``∂²F/∂x²`` on ``I_x = [x_min, x_max]``. With other
coordinates ranging over finite ``H_h``, the product of boxes is a compact
continuum *slice of* ``ℍ̃`` covering the observed scale range (the half-line
``x > x_max`` is handled by structural ``ord``, not by this test).

These enclosures are the substrate for soft violation scores ``v_a`` in
``src.search.soft`` (``sec:soft``)—not a search-time reject filter. The
sufficient inequalities of eq. interval-bb hold precisely when the corresponding
gaps vanish (and ``F̄ < ∞``):

    ``∂F/∂x̄ ≤ 0``,          # (A1) / stage (i)  ↔  v_mono = 0
    ``∂²F/∂x²̲ ≥ 0``,         # (A2) / stage (ii) ↔  v_conv = 0
    ``F̲ > L_∞``,             # (A3) / (iv)  ↔  v_irred = 0  (⇒ (iii) if L_∞ > 0)
    ``F̄ < ∞``.              # finiteness half of (A5)/(vi)

This is a *sufficient* certificate that the continuum conditions hold
everywhere on ``I_x`` (one-sided: large gaps do not prove inadmissibility).
Pair with structural checks from ``ia_eval`` for condition (v) / the ``x→∞``
tail.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from src.constraints.certificates.interval import DualInterval, Interval


@dataclass(frozen=True)
class IntervalCertificate:
    """IA enclosures on one or more axes (eq. interval-bb).

    Soft search reads ``enclosures`` to build ``v_a`` (including the joint-floor
    gap via ``v_irred``). ``zero_gap`` is an optional diagnostic equivalent to
    ``V``-related gaps vanishing on the box (not a search gate).
    """

    enclosures: dict[str, DualInterval]
    zero_gap: bool = False
    reasons: tuple[str, ...] = ()


class IntervalArithmeticCertificate(ABC):
    """Certificate (a) of ``sec:stage-admiss`` / ``sec:certificates``.

    Soft search calls ``certify`` (or an equivalent enclosure helper) to obtain
    DualIntervals on each ``I_x ⊂ ℍ̃`` for the violation scores of ``sec:soft``.
    """

    @abstractmethod
    def certify(
        self,
        candidate: Any,
        ensemble_ia: dict[str, DualInterval],
        domains: dict[str, Interval],
        L_inf: float,
        *args: Any,
        **kwargs: Any,
    ) -> IntervalCertificate:
        """Return DualInterval enclosures for ``g`` on each ``I_x``.

        ``domains`` should supply the scale box ``I_x`` and ranges for frozen
        coordinates so the product of boxes sits inside ``ℍ̃``.
        """
