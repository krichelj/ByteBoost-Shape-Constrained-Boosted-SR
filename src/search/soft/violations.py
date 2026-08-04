"""
Soft-search per-axiom violation scores (``sec:soft``, eq. violations-bb).

Provenance ("Where the penalties come from", ``sec:soft``). ``v_mono``,
``v_conv``, ``v_irred`` are the monotonicity / convexity / image-bound
constraints of shape-constrained symbolic regression (Kronberger et al. 2022,
doi:10.1162/evco_a_00294; SMT-based variant in Błądek & Krawiec 2019,
doi:10.1145/3321707.3321743), with two deliberate changes:

* they are evaluated on the *ensemble* ``F = L̂^{(j−1)} + g``, not on ``g``
  alone — what makes them meaningful stagewise (``prop:stage-iff``);
* violations are *penalized* in the fitness rather than rejected by a hard
  feasibility filter as in Kronberger et al., following the penalized-objective
  treatment of Martinek et al. 2024 (doi:10.1007/978-3-032-25305-7_16).

The one-sidedness of IA enclosures (they may penalize an admissible candidate,
never certify an inadmissible one) is *pessimistic* constraint evaluation in
the sense of Haider et al. 2022 (doi:10.1145/3512290.3528714); soundness is
what ``thm:guarantee`` needs, so the pessimistic side is chosen on purpose.

``v_decay`` and ``v_leaf`` have no counterpart in that literature: they encode
the scaling-law-specific rate axiom A4 via the structural exponent
``ord(g, x)`` on the half-line ``x > x_max``, not via an interval bound.

Using IA enclosures of ``F = L̂^{(j−1)} + g`` on compact slices ``I_x ⊂ ℍ̃``
and structural quantities for the ``x → ∞`` tail:

    v_mono(g)  = max_{x∈{N,D}} max(0,  ∂F/∂x̄)     # (A1) / stage (i)
    v_conv(g)  = max_{x∈{N,D}} max(0, −∂²F/∂x²̲)    # (A2) / stage (ii)
    v_irred(g) = max_{x∈{N,D}} max(0, L_∞ − F̲)  # (A3) / stage (iv); ⇒ (iii) if L_∞ > 0
    v_decay(g) = max_{x∈{N,D}} max(0, ord(g,x) − c_x^{(0)} + ε_decay)  # (A4)/(v)
    v_leaf(g)  = |{x ∈ {N,D} : x ∉ leaves(g)}|  # prerequisite for ord

Every score is nonnegative. Aggregate ``V(g) = Σ_a v_a(g)``.
Soft fitness uses ``Σ_a λ_a v_a(g)²`` (typically with positive ``λ``); ``λ = 0``
is the unconstrained ablation. Soft scores act as IA proxies for A1–A4;
A5 is discharged by DualInterval finiteness / the ``C²`` (in practice
``C^∞``) operator set — not a separate ``v_a``. ``V = 0`` with finite
enclosures implies certificates (a)–(b) and the boosting guarantee
(match ``AXIOM_INDICES`` / your λ schedule).
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
