"""
Stage-0 generalized Chinchilla law (``sec:boosting``, Prop. 1 / ``prop:chinchilla-admiss``,
eq. chinchilla-bb).

The 2D core ``E + A·N^-α + B·D^-β`` is the Chinchilla parametric form of
Hoffmann et al. 2022 (arXiv:2203.15556, eq. 2), generalized here to extra
hyperparameter axes; ``E`` is their irreducible loss (entropy of natural text).
The stagewise-additive ensemble around it is gradient boosting in the sense of
Friedman 2001 (doi:10.1214/aos/1013203451), with shape-constrained search
(``sec:soft``) in place of an unconstrained base learner.

Stage 0 fits by nonlinear least squares (positive parameter constraints) an
admissible baseline on the labeled grid ``ℍ``. The closed-form law extends to
the continuum domain ``ℍ̃`` and lies in ``S`` (A1)–(A5). The canonical power-law
form is

    L̂^{(0)} = L̂_0
            = A / N^α + B / D^β + Σ_{i=1}^m C_i / φ_i(h_i)^{γ_i} + E,

    with all coefficients/exponents positive. By construction:
* joint floor ``L_∞ = E`` (joint limit as all scales → ∞), which already
  forces ``L̂_0 > 0`` on ``ℍ̃``;
* stage-0 asymptotic exponents ``c_N^{(0)} = −α``, ``c_D^{(0)} = −β``;
* graceful saturation (A5): power maps are ``C^∞`` (hence ``C²``) on
  ``[x_min, ∞)``.

Concrete grids: 2D ``(N, D)`` and 4D ``(N, D, WD, lr)``. For 4D, hyperparameter
terms may instead be quadratic penalties in ``log φ_lr(lr)`` /
``log φ_wd(wd)`` (U-shaped loss in the preprocessed log features); shape
axioms still act only on ``N`` and ``D``.

``evaluate_ia`` should return DualInterval images on certification boxes
``I_x ⊂ ℍ̃`` for use as the stage-0 contribution to ensemble enclosures.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from src.constraints.certificates.interval import DualInterval, Interval


class BaselineFit(ABC):
    """Admissible stage-0 approximant ``L̂_0 ∈ S`` on ``ℍ̃``."""

    @abstractmethod
    def fit(self, X: Any, y: Any) -> None:
        """Fit positive coefficients of eq. chinchilla-bb on labeled pairs."""

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
        """IA+AD image of ``L̂_0`` on a box in ``ℍ̃``, differentiating w.r.t. ``diff_var``."""


class GeneralizedChinchilla(BaselineFit):
    """Concrete stage-0 law; implement 2D and/or 4D specializations."""

    def fit(self, X: Any, y: Any) -> None:
        raise NotImplementedError("TODO: NLS fit of eq. chinchilla-bb with positive params")

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
        raise NotImplementedError("TODO: DualInterval evaluation of L̂_0 on I_x ⊂ ℍ̃")
