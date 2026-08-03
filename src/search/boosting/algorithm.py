"""
Boosted ensemble construction (``sec:boosting``, Algorithm ``alg:boosting-bb``).

Admissibility invariant: ``L̂^{(j)} ∈ S`` for every ``j = 0, …, K``.
Notation: ``L̂_j`` (subscript) = stage-``j`` correction;
``L̂^{(j)}`` (superscript) = cumulative ensemble through stage ``j``,
with ``L̂^{(0)} = L̂_0``.

Algorithm
---------
1. Fit ``L̂_0`` via eq. chinchilla; set ``L̂^{(0)} ← L̂_0``.
2. For ``j = 1, …, K``:
   a. Compute ``δ_j`` and Huber pseudo-residuals ``r̃_j^{(ℓ)}``.
   b. Find ``L̂_j`` via the soft penalized objective of ``sec:soft``
      (primary), or via hard certificates (a)–(b) of ``sec:stage-admiss``
      (workshop extension).
   c. ``L̂^{(j)} ← L̂^{(j−1)} + L̂_j``.
3. Return ``L̂^{(K)} ∈ S``.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class EnsembleState:
    """Running state of ``L̂^{(j)}`` during boosting."""

    stage_index: int = 0
    joint_floor: float | None = None  # L_∞ (= E under the hard path)
    stage0_exponents: dict[str, float] = field(default_factory=dict)  # c_x^{(0)}
    corrections: list[Any] = field(default_factory=list)  # L̂_1, …, L̂_j
    # Students may store programs, IA caches, metrics, …


class BoostingAlgorithm(ABC):
    """Shape-constrained boosted symbolic regression (Algorithm 1)."""

    def __init__(self, num_stages: int, baseline: Any, search_backend: Any):
        """
        Parameters
        ----------
        num_stages:
            ``K`` — number of correction stages after stage 0.
        baseline:
            Stage-0 ``BaselineFit`` (``src.search.baselines``).
        search_backend:
            Soft stage search by default (``src.search.soft_path``);
            optional hard reject filter (``src.search.hard_path``).
        """
        self.K = num_stages
        self.baseline = baseline
        self.search_backend = search_backend
        self.state = EnsembleState()

    def fit(self, dataset: Any, *args: Any, **kwargs: Any) -> EnsembleState:
        """Run Algorithm 1 on labeled dataset ``D``; return final ensemble state."""
        raise NotImplementedError("TODO: implement alg:boosting-bb")

    def predict(self, X: Any) -> Any:
        """Evaluate ``L̂^{(K)}(h)``."""
        raise NotImplementedError("TODO: sum baseline + corrections")

    @abstractmethod
    def _fit_stage(
        self,
        X: Any,
        pseudo_residuals: Any,
        stage_index: int,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """Return stage-``j`` correction ``L̂_j`` (expression + predictor)."""
