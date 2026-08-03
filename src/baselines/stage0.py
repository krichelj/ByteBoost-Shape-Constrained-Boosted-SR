"""
Stage-0 generalized Chinchilla law (``sec:boosting``, eq. chinchilla).

Stage 0 fits, in closed form / nonlinear least squares, an admissible baseline

    L̂^{(0)} = L̂_0
            = A / N^α + B / D^β + Σ_{i=1}^m C_i / φ_i(h_i)^{γ_i} + E,

with all coefficients/exponents positive. By construction:
* joint floor ``L_∞ = E``;
* stage-0 asymptotic exponents ``c_N^{(0)} = −α``, ``c_D^{(0)} = −β``.

Hyperparameter terms (``m``, ``φ_i``, …) depend on the chosen grid
(2D vs 4D, etc.) — choose a concrete parameterization in subclasses.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from src.certificates.interval import DualInterval, Interval


class BaselineFit(ABC):
    """Admissible stage-0 approximant ``L̂_0 ∈ S``."""

    @abstractmethod
    def fit(self, X: Any, y: Any) -> None:
        """Fit positive coefficients of eq. chinchilla on labeled pairs."""

    @abstractmethod
    def predict(self, X: Any) -> Any:
        """Evaluate ``L̂_0(h)`` on configurations stacked in ``X``."""

    @property
    @abstractmethod
    def params(self) -> dict[str, float]:
        """Fitted symbols ``A, B, C_i, E, α, β, γ_i, …``."""

    @property
    @abstractmethod
    def expression(self) -> str:
        """Human-readable formula string for reporting / deliverables."""

    @property
    @abstractmethod
    def L_inf(self) -> float:
        """Joint floor ``L_∞ = E``."""

    @abstractmethod
    def asymptotic_exponent(self, scale_var: str) -> float:
        """Return ``c_x^{(0)}`` for ``scale_var ∈ {\"N\", \"D\"}``."""

    @abstractmethod
    def evaluate_ia(
        self,
        raw_domains: dict[str, Interval],
        diff_var: str,
    ) -> DualInterval:
        """IA+AD image of ``L̂_0`` differentiating w.r.t. ``diff_var``."""


class GeneralizedChinchilla(BaselineFit):
    """Concrete stage-0 law — implement 2D and/or 4D specializations."""

    def fit(self, X: Any, y: Any) -> None:
        raise NotImplementedError("TODO: fit eq. chinchilla with positive params")

    def predict(self, X: Any) -> Any:
        raise NotImplementedError("TODO: evaluate L̂_0")

    @property
    def params(self) -> dict[str, float]:
        raise NotImplementedError

    @property
    def expression(self) -> str:
        raise NotImplementedError

    @property
    def L_inf(self) -> float:
        raise NotImplementedError

    def asymptotic_exponent(self, scale_var: str) -> float:
        raise NotImplementedError("TODO: −α or −β")

    def evaluate_ia(
        self,
        raw_domains: dict[str, Interval],
        diff_var: str,
    ) -> DualInterval:
        raise NotImplementedError("TODO: DualInterval evaluation of L̂_0")
