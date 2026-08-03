"""
Soft search backends (``sec:software``, ``sec:soft``).

The project description names Deep Symbolic Optimization (DSO) with a
transformer-based controller for the soft-constrained path, and also allows
a gplearn-style search with soft IA penalties in the fitness. Implement at
least one backend; comparing them is a natural workshop slice.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class SoftSearchBackend(ABC):
    """Minimize penalized fitness ``F_j`` over expression trees."""

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
    """Soft IA penalties inside a gplearn-style fitness."""

    def fit_stage(
        self,
        X: Any,
        pseudo_residuals: Any,
        ensemble_state: Any,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        raise NotImplementedError(
            "TODO: patch / supply fitness = MSE + Σ λ_a v_a² during GP search"
        )


class DSOBackend(SoftSearchBackend):
    """Deep Symbolic Optimization controller (named soft engine in ``sec:software``)."""

    def fit_stage(
        self,
        X: Any,
        pseudo_residuals: Any,
        ensemble_state: Any,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        raise NotImplementedError(
            "TODO: wire DSO / transformer controller with soft violation rewards"
        )
