"""
Sound interval certificates on the compact box ``I_x`` (``sec:certificates``,
eq. interval-bb).

Let ``F = L̂^{(j−1)} + g``. Forward-mode AD + IA returns enclosures of
``F``, ``∂F/∂x``, ``∂²F/∂x²`` on ``I_x = [x_min, x_max]``. With other
coordinates ranging over finite ``H_h``, the product of boxes is a compact
continuum *slice of* ``ℍ̃`` covering the observed scale range (the half-line
``x > x_max`` is handled by structural ``ord``, not by this test).

Accept ``g`` when, for each ``x ∈ {N, D}``:

    ``∂F/∂x̄ ≤ 0``,          # (A1) / stage (i)
    ``∂²F/∂x²̲ ≥ 0``,         # (A2) / stage (ii)
    ``F̲ > L_∞``,             # (A3)/(A5) / stage (iv)⇒(iii)
    ``F̄ < ∞``.              # finiteness half of (A6)/(vi);
                              # C² (in practice C^∞) from the operator set

This is a *sufficient* certificate that the corresponding continuum conditions
hold everywhere on ``I_x`` (one-sided: failure does not prove inadmissibility).
Pair with structural checks from ``ia_eval`` for condition (v) / the ``x→∞`` tail.

Despite the ``Hard*`` class name, the *enclosures* are shared infrastructure:
the soft path (``sec:soft``) converts the same bounds into continuous
``v_mono``, ``v_conv``, ``v_irred`` scores rather than a boolean reject gate.
The hard path (workshop extension) uses ``passed`` as a reject filter.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from src.constraints.certificates.interval import DualInterval, Interval


@dataclass(frozen=True)
class IntervalCertificate:
    """Result of the sufficient IA test (eq. interval-bb) on one or more axes.

    Soft path: read ``enclosures`` to build ``v_a`` (including floor/positivity
    via ``v_irred``). Hard path: use ``passed``.
    """

    passed: bool
    enclosures: dict[str, DualInterval]
    reasons: tuple[str, ...] = ()


class HardIntervalCertificate(ABC):
    """Certificate (a) of ``sec:stage-admiss`` / ``sec:certificates``.

    Name is historical for the boolean gate; soft search still calls
    ``certify`` (or an equivalent enclosure helper) to obtain DualIntervals
    on each ``I_x ⊂ ℍ̃``.
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
        """Return whether ``g`` passes the sufficient IA filter on each ``I_x``.

        ``domains`` should supply the scale box ``I_x`` and ranges for frozen
        coordinates so the product of boxes sits inside ``ℍ̃``.
        """
