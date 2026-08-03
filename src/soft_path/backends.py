"""
Soft search backends (``sec:software``, ``sec:soft``).

The project description names Deep Symbolic Optimization (DSO) with a
transformer-based controller for the soft-constrained path. The reference
submodule instead implements soft IA penalties inside gplearn. Both are valid
student targets: implement at least one; the DSO stub captures the named engine.
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
    """Soft IA penalties inside a gplearn-style fitness (reference approach)."""

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
