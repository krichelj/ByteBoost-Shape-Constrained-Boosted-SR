"""
Stagewise admissibility of an increment (``sec:stage-admiss``, Prop. 2 /
``prop:stage-iff``, eq. stage-admiss-bb).

Given ``L̂^{(j−1)} ∈ S`` with joint floor ``L_∞`` and stage-0 rates ``c_x^{(0)}``,
the update ``L̂^{(j)} = L̂^{(j−1)} + L̂_j`` is admissible with the same floor and
the same rates **if** the increment ``g = L̂_j`` satisfies, for each scale
``x ∈ {N, D}``:

(i)   ``∂g/∂x ≤ −∂L̂^{(j−1)}/∂x`` for all ``x ≥ x_min``
(ii)  ``∂²g/∂x² ≥ −∂²L̂^{(j−1)}/∂x²`` for all ``x ≥ x_min``
(iii) ``g(h) > −L̂^{(j−1)}(h)`` for all ``h ∈ ℍ̃``
(iv)  ``L̂^{(j−1)}(h) + g(h) > L_∞`` for all ``h ∈ ℍ̃``
(v)   ``g(h)|_{x=t} = O(t^{c_{x,j}})`` as ``t → ∞`` for some
      ``c_{x,j} < c_x^{(0)}`` (implied by ``ord(g, x) < c_x^{(0)}``)
(vi)  ``g ∈ C^∞`` on ``[x_min, ∞)`` with ``|g(x_min, ·)| < ∞``

These are sufficient, not necessary: the converse gives (i)–(iv), (vi) plus only
the weaker tail bound ``g|_{x=t} = o(t^{c_x^{(0)}})``. Condition (v) is the
strictly stronger form — it rules out borderline tails like ``t^{c_x^{(0)}}/log t``
— and is used because it is what ``ord`` decides exactly on a finite tree. Only
the sufficient direction is needed by ``thm:guarantee``.

When ``L_∞ > 0``, (iv) already implies (iii); both are kept so ensemble
positivity and floor preservation stay explicit. ``ℍ̃`` is the continuum domain
of ``sec:setup`` (scales on ``[x_min, ∞)``, other coords in finite ``H_h``).

Note (vi) is on the **whole half-line**, not just the certification box: the (A5)
half of prop:stage-iff needs ``L̂^{(j−1)} + g`` to stay ``C²`` wherever (A1)–(A2)
are asserted. For a finite tree that means no division denominator and no
``pow_p`` argument vanishes on ``[x_min, ∞)``. IA discharges this on ``I_x``
(a finite enclosure implies no such subtree vanished there); past ``x_max`` it is
a structural side condition — restrict divisors to subtrees of certified sign, or
widen ``I_x`` past the range you actually report extrapolations over.

Conditions (i)–(iv), (vi) on the compact box ``I_x ⊂ ℍ̃`` are handled by sound
interval enclosures (A1–A3/A5 on the observed scale range); (v) by the
structural exponent ``ord(g, x)`` for the ``x → ∞`` tail
(see ``src.constraints.certificates``). Soft search (``sec:soft`` /
``src.search.soft``) turns those quantities into continuous ``v_a`` that enter
the fitness—the sole discovery method. This module scores increments; it is
not a search-time accept/reject filter.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class StageAdmissibilityScores:
    """Soft scores / diagnostics for stage conditions (i)–(vi) on ``g``.

    Prefer ``violations`` / ``V`` for search. ``zero_penalty`` is a derived
    diagnostic (``V == 0`` with finite DualInterval enclosures), not a gate.
    """

    violations: Mapping[str, float]
    V: float
    zero_penalty: bool = False
    details: dict[str, Any] = field(default_factory=dict)


class StageAdmissibilityScorer(ABC):
    """Score how far ``g`` is from preserving ensemble admissibility."""

    @abstractmethod
    def score(
        self,
        candidate: Any,
        ensemble_state: Any,
        *args: Any,
        **kwargs: Any,
    ) -> StageAdmissibilityScores:
        """
        Parameters
        ----------
        candidate:
            Expression tree / program ``g`` (representation is student-defined).
        ensemble_state:
            Enough information to evaluate ``L̂^{(j−1)}`` and its IA image
            (floors, prior programs, domains ``I_x``, exponents ``c_x^{(0)}``, …).
        """
