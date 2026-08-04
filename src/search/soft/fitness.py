"""
Soft-search penalized fitness (``sec:soft``, Prop. 3 / ``prop:soft``:
zero-penalty ⇒ certificates; eq. penalized-bb).

Stage ``j`` minimizes

    F_j(g) = (1/n) Σ_ℓ (r̃_j^{(ℓ)} − g(h_ℓ))²  +  Σ_a λ_a v_a(g)²

The first term is data fit to Huber pseudo-residuals on the labeled grid ``ℍ``;
the second penalizes axiom gaps from DualInterval certificates on compact
slices ``I_x ⊂ ℍ̃`` (plus structural ``ord`` / leaf scores). Squared so the
penalty gradient vanishes at zero violation.
Candidates that already satisfy stage admissibility incur no penalty pressure.

Guarantee sketch (see description): ``V = 0`` plus finite DualInterval
enclosures implies certificates (a)–(b) and the boosting guarantee on ``ℍ̃``;
``v_irred`` covers joint floor (A3) and positivity (A5); A6 is discharged by
successful finite IA under the ``C^∞`` operator set (not a separate ``v_a``);
interval-based scores upper-bound true pointwise violations on ``I_x``.
"""

from __future__ import annotations

from typing import Any, Mapping

from src.scaling.setup.constants import DEFAULT_LAMBDAS


def penalized_fitness(
    y_residuals: Any,
    y_pred: Any,
    violations: Mapping[str, float],
    lambdas: Mapping[str, float] | None = None,
) -> float:
    """Evaluate scalar fitness ``F_j(g)`` (eq. penalized-bb).

    Parameters
    ----------
    y_residuals, y_pred:
        Huber targets ``r̃_j`` and candidate predictions ``g(h_ℓ)``.
    violations:
        ``v_a(g)`` from ``compute_violations`` (IA on ``I_x ⊂ ℍ̃`` + ``ord``).
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
