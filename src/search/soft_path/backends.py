"""
Soft search backends (``sec:software``, ``sec:soft``).

Primary engine: ``gplearn`` with IA axiom penalties in the fitness
(``GPLearnSoftBackend``). Optional: PySR as an unconstrained / post-hoc
ablation backend. A hard reject filter is a separate workshop extension
(``src.search.hard_path``), not a second soft engine.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class SoftSearchBackend(ABC):
    """Minimize penalized fitness ``F_j`` over expression trees.

    ``X`` is typically the log-feature matrix ``log φ_h(h)``; targets are Huber
    pseudo-residuals ``r̃_j``. ``ensemble_state`` carries ``L̂^{(j−1)}`` context
    (floor, stage-0 exponents, prior programs) needed to score ``v_a``.
    """

    @abstractmethod
    def fit_stage(
        self,
        X: Any,
        pseudo_residuals: Any,
        ensemble_state: Any,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """Return a correction ``g`` found under soft axiom penalties."""


class GPLearnSoftBackend(SoftSearchBackend):
    """Primary soft path: patch gplearn fitness with MSE + Σ λ_a v_a²."""

    def fit_stage(
        self,
        X: Any,
        pseudo_residuals: Any,
        ensemble_state: Any,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        raise NotImplementedError(
            "TODO: install IA-penalized raw_fitness during SymbolicRegressor.fit"
        )


class PySRSoftBackend(SoftSearchBackend):
    """Optional PySR engine (typically unconstrained; score V post hoc)."""

    def fit_stage(
        self,
        X: Any,
        pseudo_residuals: Any,
        ensemble_state: Any,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        raise NotImplementedError("TODO: fit PySR stage; optionally report V after the fact")
