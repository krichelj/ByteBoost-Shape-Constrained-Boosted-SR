"""
Optional JAX + custom JVP certificate path (``sec:software``).

The project description lists JAX with custom JVP rules and a Python
interval-arithmetic backend for the AD+IA proof step. The reference submodule
uses pure-Python ``DualInterval`` instead. Students may implement either (or
both) behind the same ``HardIntervalCertificate`` interface.
"""

from __future__ import annotations

from typing import Any

from src.certificates.hard_certificates import HardIntervalCertificate, IntervalCertificate
from src.certificates.interval import DualInterval, Interval


class JaxIntervalCertificate(HardIntervalCertificate):
    """Certificate (a) evaluated with JAX JVPs composed with interval bounds."""

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
            "TODO: optional JAX JVP + IA backend implementing eq. interval"
        )
