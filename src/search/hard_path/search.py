"""
Hard-constrained search path (``sec:stage-admiss``, workshop extension).

Reject inadmissible corrections during search so that only candidates ``g`` that
pass certificates (a)–(b) enter the stage argmin

    L̂_j ∈ argmin_g (1/n) Σ_ℓ (r̃_j^{(ℓ)} − g(h_ℓ))²
          subject to certificates (a)–(b).

The primary shipped method is the soft-penalty gplearn path
(``src.search.soft_path``, ``sec:soft``). Implement this hard filter on top of
the same DualInterval certificate helpers (IA on ``I_x ⊂ ℍ̃``, structural
``ord`` for the ``x→∞`` tail).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class HardSearchBackend(ABC):
    """Symbolic regression that discards candidates failing hard certificates."""

    @abstractmethod
    def fit_stage(
        self,
        X: Any,
        pseudo_residuals: Any,
        ensemble_state: Any,
        certificate: Any,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Search expression trees; return an admissible correction ``g = L̂_j``.

        Parameters
        ----------
        X, pseudo_residuals:
            Features (typically log-features) and Huber targets ``r̃_j``.
        ensemble_state:
            ``L̂^{(j−1)}`` context (floors, exponents, prior programs,
            certification domains ``I_x ⊂ ℍ̃``).
        certificate:
            Object implementing sufficient IA + structural checks
            (``src.constraints.certificates``, ``src.constraints.axioms.stage_conditions``).
        """


class GPLearnHardBackend(HardSearchBackend):
    """Hard filter wired into a gplearn-style population search."""

    def fit_stage(
        self,
        X: Any,
        pseudo_residuals: Any,
        ensemble_state: Any,
        certificate: Any,
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        raise NotImplementedError(
            "TODO: run GP search; reject g that fail certificates (a)–(b); "
            "return argmin among survivors"
        )
