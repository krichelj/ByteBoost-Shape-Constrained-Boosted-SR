"""
Helpers for the cumulative map ``L̂^{(j)} = L̂^{(j−1)} + L̂_j`` (``sec:algorithm``,
``alg:boosting-bb``).

Algorithm 1 maintains a running ensemble predictor on ``ℍ̃``: stage 0 is the
Chinchilla baseline ``L̂_0``, and each later stage adds a symbolic correction
``L̂_j`` found by soft (primary) or hard (workshop) search. These helpers
compose callables for prediction and for DualInterval evaluation of
``F = L̂^{(j−1)} + g`` on certification boxes ``I_x ⊂ ℍ̃``.
"""

from __future__ import annotations

from typing import Any, Callable, Sequence


def add_correction(
    previous_predict: Callable[[Any], Any],
    correction_predict: Callable[[Any], Any],
) -> Callable[[Any], Any]:
    """Return a callable for ``h ↦ L̂^{(j−1)}(h) + g(h)``."""
    raise NotImplementedError("TODO: pointwise sum of predictors")


def compose_ensemble(
    baseline_predict: Callable[[Any], Any],
    corrections: Sequence[Callable[[Any], Any]],
) -> Callable[[Any], Any]:
    """Compose ``L̂^{(K)} = L̂_0 + Σ_{j=1}^K L̂_j``."""
    raise NotImplementedError("TODO: fold corrections onto the baseline")
