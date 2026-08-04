"""
Soft search backends (``sec:software``, ``sec:soft``).

Primary engine: ``gplearn`` with IA axiom penalties in the fitness
(``GPLearnSoftBackend``). Penalties use DualInterval enclosures on compact
slices ``I_x ⊂ ℍ̃`` (``I_x`` ≡ ``ℐ_x`` in the PDF) plus structural ``ord`` /
leaf scores: A1–A4 via ``v_mono…v_decay``, leaf for scale presence, and A5
discharged by finite DualInterval enclosures under the ``C^∞`` operator set
(not a separate ``v_a``).

Optional: PySR as an unconstrained / post-hoc ablation backend.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class SoftSearchBackend(ABC):
    """Minimize penalized fitness ``F_j`` over expression trees.

    ``X`` is typically the log-feature matrix ``log φ_h(h)`` on labeled ``ℍ``;
    targets are Huber pseudo-residuals ``r̃_j``. ``ensemble_state`` carries
    ``L̂^{(j−1)}`` context (floor, stage-0 exponents, prior programs, ``I_x``
    domains in ``ℍ̃``) needed to score ``v_a``.
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
    """gplearn fitness with MSE + Σ λ_a v_a² (sole discovery engine of ``sec:soft``)."""

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
    """Optional PySR engine (typically unconstrained; score V post hoc on ℍ̃)."""

    def fit_stage(
        self,
        X: Any,
        pseudo_residuals: Any,
        ensemble_state: Any,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        raise NotImplementedError("TODO: fit PySR stage; optionally report V after the fact")
