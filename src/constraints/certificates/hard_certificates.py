"""
Sound interval certificates on the compact box ``I_x`` (eq. interval).

Let ``F = L̂^{(j−1)} + g``. Forward-mode AD + IA returns enclosures of
``F``, ``∂F/∂x``, ``∂²F/∂x²`` on ``I_x = [x_min, x_max]``. Accept ``g`` when,
for each ``x ∈ {N, D}``:

    ``∂F/∂x̄ ≤ 0``,
    ``∂²F/∂x²̲ ≥ 0``,
    ``F̲ > L_∞``,
    ``F̄ < ∞``.

This is a *sufficient* certificate that the corresponding continuum conditions
hold everywhere on ``I_x`` (one-sided: failure does not prove inadmissibility).
Pair with structural checks from ``ia_eval`` for condition (v) / the ``x→∞`` tail.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from src.constraints.certificates.interval import DualInterval, Interval


@dataclass(frozen=True)
class IntervalCertificate:
    """Result of the sufficient IA test (eq. interval) on one or more axes."""

    passed: bool
    enclosures: dict[str, DualInterval]
    reasons: tuple[str, ...] = ()


class HardIntervalCertificate(ABC):
    """Certificate (a) of ``sec:stage-admiss`` / ``sec:certificates``."""

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
        """Return whether ``g`` passes the sufficient IA filter on each ``I_x``."""
