"""
Helpers for the cumulative map ``L̂^{(j)} = L̂^{(j−1)} + L̂_j``.
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
