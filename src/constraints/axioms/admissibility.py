"""
Admissibility axioms (A1)–(A6) (project description ``sec:axioms``).

Although the labeled grid ``ℍ`` is finite, ``L̂`` is constrained on the continuum
domain ``ℍ̃`` of ``sec:setup``: each scale ranges over ``[x_min, ∞)``, other
coordinates over finite ``H_h``, with ``ℍ ⊂ ℍ̃``.

A scaling-law approximant ``L̂`` is *admissible* (``L̂ ∈ S``) when it satisfies:

(A1) **Monotone decrease.**
    ``∂L̂/∂x ≤ 0`` for all ``x ≥ x_min`` (each scale ``x ∈ {N, D}``).

(A2) **Diminishing returns.**
    ``∂²L̂/∂x² ≥ 0`` for all ``x ≥ x_min``.
    Together with (A1): further increases in ``x`` yield weakly smaller loss
    reductions.

(A3) **Irreducible loss.**
    Joint floor ``L_∞ > 0`` with ``L̂(h) > L_∞`` for every ``h ∈ ℍ̃``;
    marginal floors (eq. margfloor-bb)
    ``L^∞_x = lim_{t→∞} L̂(h)|_{x=t}`` exist, are finite, and satisfy
    ``L^∞_x ≥ L_∞``.  (``L^∞_x`` depends on the frozen coordinates.)
    In the stage-0 Chinchilla law, ``L_∞ = E`` is the joint limit as all scales
    → ∞; a single-axis marginal is typically strictly larger.

(A4) **Asymptotic power-law decay** (eq. powerlaw-bb).
    Relative to the marginal floor,
    ``lim_{t→∞} log(L̂(h)|_{x=t} − L^∞_x) / log t = c_x`` for some ``c_x < 0``.
    The excess is eventually positive (log defined) when the marginal floor is
    approached from above under (A1).

(A5) **Positivity.** ``L̂(h) > 0`` for every ``h ∈ ℍ̃``.
    Implied by (A3) when ``L_∞ > 0``; retained as an explicit prior.
    Soft search (``sec:soft``) folds (A5) into ``v_irred``.

(A6) **Graceful saturation.** ``L̂`` is ``C²`` in ``x`` on ``[x_min, ∞)``
    (so the second derivative in (A2) exists), and ``L̂(x_min, ·)`` is finite.
    Expression-tree corrections are ``C^∞`` on ``(0, ∞)``.
    ``L̂(x_min, ·) > L_∞`` is already required by (A3)(i).

Continuum statements are decided by certificates in ``src.constraints.certificates``:
sound IA on compact boxes ``I_x ⊂ ℍ̃`` (observed scale range), structural ``ord``
for the ``x → ∞`` tail.

Soft-search scores (``sec:soft``, eq. violations-bb) cover A1–A4 via
``mono / conv / irred / decay``, plus ``leaf`` for scale presence in the tree;
A5 is folded into the irreducible-floor gap and A6 into DualInterval
finiteness / the ``C²`` (in practice ``C^∞``) operator set (``V = 0`` with
finite enclosures implies certificates (a)–(b) and the boosting guarantee).
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
        """Attempt to certify (A1)–(A6); details of evidence are student-defined."""
