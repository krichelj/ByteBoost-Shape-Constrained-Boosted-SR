"""
Hard-constrained search path (``sec:boosting``, ``sec:stage-admiss``).

One search method **rejects** inadmissible corrections: only candidates ``g``
that pass certificates (a)–(b) of ``sec:stage-admiss`` are eligible for the
stage argmin

    L̂_j ∈ argmin_g (1/n) Σ_ℓ (r̃_j^{(ℓ)} − g(h_ℓ))²
          subject to certificates (a)–(b).

Project software note (``sec:software``): ``gplearn`` with custom admissibility
predicates is the intended hard-path engine. Implementing a true reject filter
during search (only survivors of certificates (a)–(b) enter the stage argmin)
is a primary ByteBoost exercise.
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
            Features and Huber targets ``r̃_j`` for stage ``j``.
        ensemble_state:
            ``L̂^{(j−1)}`` context (floors, exponents, prior programs, domains).
        certificate:
            Object implementing the sufficient IA + structural checks
            (``src.certificates``, ``src.axioms.stage_conditions``).
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
