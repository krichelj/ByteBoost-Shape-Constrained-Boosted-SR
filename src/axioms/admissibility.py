"""
Admissibility axioms (A1)–(A6) (project description ``sec:axioms``).

A scaling-law approximant ``L̂`` is *admissible* (``L̂ ∈ S``) when it satisfies:

(A1) **Monotone decrease.**
    ``∂L̂/∂x ≤ 0`` for all ``x ≥ x_min`` (each scale ``x ∈ {N, D}``).

(A2) **Diminishing returns.**
    ``∂²L̂/∂x² ≥ 0`` for all ``x ≥ x_min``.

(A3) **Irreducible loss.**
    Joint floor ``L_∞ > 0`` with ``L̂(h) > L_∞`` for every ``h ∈ ℍ``;
    marginal floors ``L^∞_x = lim_{t→∞} L̂(h)|_{x=t}`` exist, are finite,
    and satisfy ``L^∞_x ≥ L_∞``.

(A4) **Asymptotic power-law decay.**
    Relative to the marginal floor,
    ``lim_{t→∞} log(L̂(h)|_{x=t} − L^∞_x) / log t = c_x`` for some ``c_x < 0``.

(A5) **Positivity.** ``L̂(h) > 0`` for all ``h ∈ ℍ``.

(A6) **Graceful saturation.** ``L̂`` is ``C¹`` in ``x`` on ``[x_min, ∞)``,
    with ``L̂(x_min, ·)`` finite and ``> L_∞``.

Continuum statements are decided by certificates in ``src.certificates``
(sound IA on the compact box ``I_x``, structural checks for asymptotics).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class AxiomReport:
    """Per-axiom pass/fail (or soft score) for a candidate ``L̂`` or increment ``g``.

    Students may store booleans for the hard path and floats for soft gaps.
    Keys should include at least the soft indices
    ``mono, conv, irred, decay, leaf`` plus any explicit A5/A6 fields.
    """

    results: Mapping[str, Any]


class AdmissibleLaw(ABC):
    """Interface for an approximant that claims membership in ``S``."""

    @abstractmethod
    def joint_floor(self) -> float:
        """Joint irreducible floor ``L_∞``."""

    @abstractmethod
    def marginal_floor(self, scale_var: str) -> float:
        """Marginal floor ``L^∞_x`` along ``scale_var ∈ {N, D}``."""

    @abstractmethod
    def asymptotic_exponent(self, scale_var: str) -> float:
        """Power-law exponent ``c_x`` (stage 0: ``c_N^{(0)} = −α``, ``c_D^{(0)} = −β``)."""

    @abstractmethod
    def check_axioms(self, *args: Any, **kwargs: Any) -> AxiomReport:
        """Attempt to certify (A1)–(A6); details of evidence are student-defined."""
