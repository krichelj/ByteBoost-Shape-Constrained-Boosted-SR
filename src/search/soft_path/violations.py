"""
Soft-path per-axiom violation scores (``sec:soft``, eq. violations).

Using IA enclosures of ``F = L̂^{(j−1)} + g`` and structural quantities:

    v_mono(g)  = max_{x∈{N,D}} max(0,  ∂F/∂x̄)
    v_conv(g)  = max_{x∈{N,D}} max(0, −∂²F/∂x²̲)
    v_irred(g) = max(0, L_∞ − F̲)
    v_decay(g) = max_{x∈{N,D}} max(0, ord(g,x) − c_x^{(0)} + ε_decay)
    v_leaf(g)  = |{x ∈ {N,D} : x ∉ leaves(g)}|

Every score is nonnegative. Aggregate ``V(g) = Σ_a v_a(g)``.
Soft fitness uses ``Σ_a λ_a v_a(g)²`` (typically with positive ``λ``); ``λ = 0``
is the unconstrained ablation. ``V = 0`` at every stage recovers hard
admissibility. A5/A6 may be folded into ``v_decay`` / ``v_leaf`` rather than
scored as separate soft terms — match ``AXIOM_INDICES`` / your λ schedule.
"""

from __future__ import annotations

from typing import Any, Mapping

from src.scaling.setup.constants import AXIOM_INDICES, EPSILON_DECAY


def compute_violations(
    candidate: Any,
    ensemble_context: Any,
    *,
    epsilon_decay: float = EPSILON_DECAY,
    **kwargs: Any,
) -> dict[str, float]:
    """Return ``{a: v_a(g)}`` for ``a`` in ``AXIOM_INDICES``.

    Parameters
    ----------
    candidate:
        Expression tree ``g``.
    ensemble_context:
        Enough state to form ``F = L̂^{(j−1)} + g`` under IA
        (baseline IA, prior stages, domains, ``L_∞``, ``c_x^{(0)}``, …).
    """
    raise NotImplementedError("TODO: implement eq. violations using DualInterval + ord")


def aggregate_violation(violations: Mapping[str, float]) -> float:
    """Return ``V(g) = Σ_a v_a(g)``."""
    raise NotImplementedError("TODO: sum axiom scores")


def assert_axiom_keys(violations: Mapping[str, float]) -> None:
    """Optional sanity check that ``violations`` covers ``AXIOM_INDICES``."""
    missing = [a for a in AXIOM_INDICES if a not in violations]
    if missing:
        raise KeyError(f"missing axiom scores: {missing}")
