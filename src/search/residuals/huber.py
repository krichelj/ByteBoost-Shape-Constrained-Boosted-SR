"""
Huber clipping and pseudo-residuals (``sec:boosting``, eq. delta-bb, eq. pseudoresid-bb).

Huber's robust loss is from Huber 1964 (doi:10.1214/aoms/1177703732); its use
as the stage target of a boosting ensemble is the Huber-M variant of gradient
boosting in Friedman 2001 (doi:10.1214/aos/1013203451).

At boosting stage ``j ≥ 1``, computed on the labeled grid ``ℍ`` (not the
continuum domain ``ℍ̃`` used by A1–A5):

    δ_j := median_{ℓ=1…n} |L(h_ℓ) − L̂^{(j−1)}(h_ℓ)|

    r̃_j^{(ℓ)} :=
        L(h_ℓ) − L̂^{(j−1)}(h_ℓ)
            if |L(h_ℓ) − L̂^{(j−1)}(h_ℓ)| ≤ δ_j,
        δ_j · sign(L(h_ℓ) − L̂^{(j−1)}(h_ℓ))
            otherwise.

Corrections ``g`` are fit to these Huber pseudo-residuals so outlier runs
cannot dominate the stage objective. Axiom gaps of ``g`` are scored via
DualInterval-derived ``v_a`` inside the soft fitness (``sec:soft``,
``src.search.soft``), the sole discovery method.
"""

from __future__ import annotations

from typing import Any


def huber_delta(y_true: Any, y_pred: Any) -> float:
    """Compute ``δ_j = median_ℓ |L(h_ℓ) − L̂^{(j−1)}(h_ℓ)|``."""
    raise NotImplementedError("TODO: median absolute residual")


def huber_pseudo_residuals(y_true: Any, y_pred: Any, delta: float) -> Any:
    """Return the vector ``(r̃_j^{(ℓ)})_{ℓ=1}^n`` (eq. pseudoresid-bb)."""
    raise NotImplementedError("TODO: clip residuals at ±delta with sign")
