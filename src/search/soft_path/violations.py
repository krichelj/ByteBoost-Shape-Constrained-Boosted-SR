"""
Soft-path per-axiom violation scores (``sec:soft``, eq. violations-bb).

Using IA enclosures of ``F = L̂^{(j−1)} + g`` on compact slices ``I_x ⊂ ℍ̃``
and structural quantities for the ``x → ∞`` tail:

    v_mono(g)  = max_{x∈{N,D}} max(0,  ∂F/∂x̄)     # (A1)
    v_conv(g)  = max_{x∈{N,D}} max(0, −∂²F/∂x²̲)    # (A2)
    v_irred(g) = max(0, L_∞ − F̲)   # (A3) floor; also (A5) when L_∞ > 0
    v_decay(g) = max_{x∈{N,D}} max(0, ord(g,x) − c_x^{(0)} + ε_decay)  # (A4)/(v)
    v_leaf(g)  = |{x ∈ {N,D} : x ∉ leaves(g)}|

Every score is nonnegative. Aggregate ``V(g) = Σ_a v_a(g)``.
Soft fitness uses ``Σ_a λ_a v_a(g)²`` (typically with positive ``λ``); ``λ = 0``
is the unconstrained ablation. Soft scores act as IA proxies for A1–A4;
positivity (A5) is folded into the irreducible-floor gap (implied by A3 when
``L_∞ > 0``) and A6 into DualInterval finiteness / the ``C²`` (in practice
``C^∞``) operator set — not a separate ``v_a``. ``V = 0`` recovers hard
certificates (a)–(b) once enclosures are finite (match ``AXIOM_INDICES`` /
your λ schedule).
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
        Enough to evaluate ``F = L̂^{(j−1)} + g`` under DualInterval
        (baseline IA, prior stages, domains ``I_x ⊂ ℍ̃``, ``L_∞``, ``c_x^{(0)}``, …).
    epsilon_decay:
        Margin in ``v_decay`` (default ``EPSILON_DECAY``).
    """
    raise NotImplementedError("TODO: implement eq. violations-bb using DualInterval + ord")


def aggregate_violation(violations: Mapping[str, float]) -> float:
    """Return ``V(g) = Σ_a v_a(g)``."""
    raise NotImplementedError("TODO: sum nonnegative axiom scores")


def assert_axiom_keys(violations: Mapping[str, float]) -> None:
    """Optional sanity check that ``violations`` covers ``AXIOM_INDICES``."""
    missing = [a for a in AXIOM_INDICES if a not in violations]
    if missing:
        raise KeyError(f"missing axiom scores: {missing}")
