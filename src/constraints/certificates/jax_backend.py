"""
Optional JAX + custom JVP certificate path (``sec:software``).

Primary certificates use pure-Python ``DualInterval``
(``src.constraints.certificates.interval`` + ``ia_eval``) on compact slices of
``ℍ̃``. This module is an optional acceleration / alternate AD+IA backend
behind the same ``IntervalArithmeticCertificate`` interface — not required for
the soft search. Must still return sound enclosures for eq. interval-bb
(including second derivatives for (A2) and floor tests for (A3)/(A5)).
"""

from __future__ import annotations

from typing import Any

from src.constraints.certificates.ia_certificates import (
    IntervalArithmeticCertificate,
    IntervalCertificate,
)
from src.constraints.certificates.interval import DualInterval, Interval


class JaxIntervalCertificate(IntervalArithmeticCertificate):
    """Optional certificate (a) with JAX JVPs composed with interval bounds."""

    def certify(
        self,
        candidate: Any,
        ensemble_ia: dict[str, DualInterval],
        domains: dict[str, Interval],
        L_inf: float,
        *args: Any,
        **kwargs: Any,
    ) -> IntervalCertificate:
        raise NotImplementedError(
            "TODO: optional JAX JVP + IA backend implementing eq. interval-bb"
        )
