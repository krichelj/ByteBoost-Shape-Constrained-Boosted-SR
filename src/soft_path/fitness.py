"""
Soft-path penalized fitness (``sec:soft``, eq. penalized).

Stage ``j`` minimizes

    F_j(g) = (1/n) Σ_ℓ (r̃_j^{(ℓ)} − g(h_ℓ))²  +  Σ_a λ_a v_a(g)²

The first term is data fit to Huber pseudo-residuals; the second penalizes
axiom gaps (squared so the penalty gradient vanishes at zero violation).
Candidates that already satisfy stage admissibility incur no penalty pressure.

Guarantee sketch (see description): ``V = 0`` recovers the hard result;
interval-based scores upper-bound true pointwise violations; for small enough
``ε_decay`` the soft search contains the hard one.
"""

from __future__ import annotations

from typing import Any, Mapping

from src.setup.constants import DEFAULT_LAMBDAS


def penalized_fitness(
    y_residuals: Any,
    y_pred: Any,
    violations: Mapping[str, float],
    lambdas: Mapping[str, float] | None = None,
) -> float:
    """Evaluate scalar fitness ``F_j(g)`` (eq. penalized).

    Parameters
    ----------
    y_residuals, y_pred:
        Huber targets ``r̃_j`` and candidate predictions ``g(h_ℓ)``.
    violations:
        ``v_a(g)`` from ``compute_violations``.
    lambdas:
        Positive weights ``λ_a``; defaults to ``DEFAULT_LAMBDAS``.
    """
    raise NotImplementedError("TODO: MSE(r̃, g) + Σ λ_a v_a²")


def fitness_breakdown(
    y_residuals: Any,
    y_pred: Any,
    violations: Mapping[str, float],
    lambdas: Mapping[str, float] | None = None,
) -> dict[str, float]:
    """Return component-wise terms for logging / debugging."""
    raise NotImplementedError("TODO: expose data-fit and per-axiom penalty terms")
