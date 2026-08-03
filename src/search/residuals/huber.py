"""
Huber clipping and pseudo-residuals (eq. delta, eq. pseudoresid).

At boosting stage ``j ≥ 1``:

    δ_j := median_{ℓ=1…n} |L(h_ℓ) − L̂^{(j−1)}(h_ℓ)|

    r̃_j^{(ℓ)} :=
        L(h_ℓ) − L̂^{(j−1)}(h_ℓ)
            if |L(h_ℓ) − L̂^{(j−1)}(h_ℓ)| ≤ δ_j,
        δ_j · sign(L(h_ℓ) − L̂^{(j−1)}(h_ℓ))
            otherwise.

Corrections ``g`` are fit to these Huber pseudo-residuals so outlier runs
cannot dominate the stage objective.
"""

from __future__ import annotations

from typing import Any


def huber_delta(y_true: Any, y_pred: Any) -> float:
    """Compute ``δ_j = median_ℓ |L(h_ℓ) − L̂^{(j−1)}(h_ℓ)|``."""
    raise NotImplementedError("TODO: median absolute residual")


def huber_pseudo_residuals(y_true: Any, y_pred: Any, delta: float) -> Any:
    """Return the vector ``(r̃_j^{(ℓ)})_{ℓ=1}^n`` (eq. pseudoresid)."""
    raise NotImplementedError("TODO: clip residuals at ±delta with sign")
