"""
Admissibility axioms (A1)–(A5) (project description ``sec:axioms``).

Provenance ("Where the axioms come from", ``sec:axioms``). A1–A4 are adopted
from the neural scaling-law literature, not posited here:

* A1/A2/A4: power-law scaling of generalization error in model and data size
  (Hestness et al. 2017, arXiv:1712.00409; Kaplan et al. 2020, arXiv:2001.08361).
* A3: the "irreducible-error region" of measured learning curves
  (Hestness et al. 2017), made explicit as ``E`` in the Chinchilla form
  ``L(N,D) = E + A·N^-α + B·D^-β`` (Hoffmann et al. 2022, arXiv:2203.15556),
  which is where ``L_∞ = E`` and ``c_N^(0) = −α``, ``c_D^(0) = −β`` get their
  published meaning.
* A5: a regularity condition, not an empirical claim: the smoothness that
  derivative-based shape constraints require (Kronberger et al. 2022,
  doi:10.1162/evco_a_00294).

Scope: A1–A2 are a modeling restriction. Non-monotonic scaling (double descent,
sharp inflections) is documented by Caballero et al. 2023 (arXiv:2210.14891);
these axioms target the smooth monotone regime of LLM pretraining loss. The
soft scores of ``sec:soft`` *measure* the admissibility gap rather than assume
it, so a testbed that violates A1–A2 shows up as a nonzero score.

Although the labeled grid ``ℍ`` is finite, ``L̂`` is constrained on the continuum
domain ``ℍ̃`` of ``sec:setup``: each scale ranges over ``[x_min, ∞)``, other
coordinates over finite ``H_h``, with ``ℍ ⊂ ℍ̃``.

A scaling-law approximant ``L̂`` is *admissible* (``L̂ ∈ S``) when it satisfies:

(A1) **Monotone decrease.**
    ``∂L̂/∂x ≤ 0`` for all ``x ≥ x_min`` (each scale ``x ∈ {N, D}``).

(A2) **Diminishing returns.**
    ``∂²L̂/∂x² ≥ 0`` for all ``x ≥ x_min``, i.e. ``L̂`` is **convex** in ``x``.
    Together with (A1): further increases in ``x`` yield weakly smaller loss
    reductions.
    Mind the direction. The textbook form of diminishing returns is *concavity*,
    but that convention is for an increasing production/utility function whose
    marginal gain falls. ``L̂`` is a decreasing *loss*, so the same shape carries
    the opposite sign, and the two agree: a gain like ``L̂(x_min, ·) − L̂`` is
    concave exactly when ``L̂`` is convex.

    Concretely, for ``L̂ = A·N^(-1/2)`` each 4x in ``N`` buys half of what the
    previous one did:

        N                 1      4      16     64
        L̂                 1.0    0.5    0.25   0.125
        gain over prev.          0.50   0.25   0.125

    The loss row flattens onto its floor, which is convex; the cumulative gain
    (0, 0.5, 0.75, 0.875) is concave. Same curve, mirrored.

    The certified quantity is the convex one throughout: (A2), stage condition
    (ii) (``∂²F/∂x² ≥ 0``), the interval test ``∂²F/∂x²̲ ≥ 0``, and
    ``v_conv = max(0, −∂²F/∂x²̲)`` all carry the same sign. Flipping it would
    contradict the stage-0 law, whose ``∂²L̂_0/∂N² = α(α+1)A·N^(-α-2)`` is
    strictly positive (``prop:chinchilla-admiss``).

(A3) **Irreducible loss.**
    Joint floor ``L_∞ > 0`` with ``L̂(h) > L_∞`` for every ``h ∈ ℍ̃``;
    marginal floors (eq. margfloor-bb)
    ``L^∞_x = lim_{t→∞} L̂(h)|_{x=t}`` exist, are finite, and satisfy
    ``L^∞_x ≥ L_∞``.  (``L^∞_x`` depends on the frozen coordinates.)
    In the stage-0 Chinchilla law, ``L_∞ = E`` is the joint limit as all scales
    → ∞; a single-axis marginal is typically strictly larger.
    Joint-floor positivity ``L_∞ > 0`` already forces ``L̂ > 0`` on ``ℍ̃``, so a
    separate positivity axiom is unnecessary.

(A4) **Asymptotic power-law decay** (eq. powerlaw-bb).
    Relative to the marginal floor,
    ``lim_{t→∞} log(L̂(h)|_{x=t} − L^∞_x) / log t = c_x`` for some ``c_x < 0``.
    The excess is eventually positive (log defined) when the marginal floor is
    approached from above under (A1).

(A5) **Graceful saturation.** ``L̂`` is ``C²`` in ``x`` on ``[x_min, ∞)``
    (so the second derivative in (A2) exists), and ``L̂(x_min, ·)`` is finite.
    Expression-tree corrections are ``C^∞`` on ``(0, ∞)``.
    ``L̂(x_min, ·) > L_∞`` is already required by (A3)(i).

Continuum statements are decided by certificates in ``src.constraints.certificates``:
sound IA on compact boxes ``I_x ⊂ ℍ̃`` (observed scale range), structural ``ord``
for the ``x → ∞`` tail.

Soft-search scores (``sec:soft``, eq. violations-bb) cover A1–A4 via
``mono / conv / irred / decay``, plus ``leaf`` for scale presence in the tree;
A5 is discharged by DualInterval finiteness / the ``C²`` (in practice ``C^∞``)
operator set (``V = 0`` with finite enclosures implies certificates (a)–(b)
and the boosting guarantee).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class AxiomReport:
    """Per-axiom soft scores (and optional diagnostics) for ``L̂`` or ``g``.

    Soft keys should include ``mono, conv, irred, decay, leaf`` (see
    ``AXIOM_INDICES``). Booleans, if present, are derived diagnostics
    (e.g. gap == 0), not a search reject gate.
    """

    results: Mapping[str, Any]


class AdmissibleLaw(ABC):
    """Interface for an approximant that claims membership in ``S``."""

    @abstractmethod
    def joint_floor(self) -> float:
        """Joint irreducible floor ``L_∞``."""

    @abstractmethod
    def marginal_floor(self, scale_var: str) -> float:
        """Marginal floor ``L^∞_x`` along ``scale_var ∈ {N, D}`` (eq. margfloor-bb).

        May depend on frozen non-``x`` coordinates; pass those via ``*args`` /
        ``**kwargs`` in your implementation if needed.
        """

    @abstractmethod
    def asymptotic_exponent(self, scale_var: str) -> float:
        """Power-law exponent ``c_x`` (stage 0: ``c_N^{(0)} = −α``, ``c_D^{(0)} = −β``)."""

    @abstractmethod
    def check_axioms(self, *args: Any, **kwargs: Any) -> AxiomReport:
        """Attempt to certify (A1)–(A5); details of evidence are student-defined."""
