"""
Stagewise admissibility of an increment (``sec:stage-admiss``, eq. stage-admiss).

Given ``L̂^{(j−1)} ∈ S`` with joint floor ``L_∞``, the update
``L̂^{(j)} = L̂^{(j−1)} + L̂_j`` is admissible **iff** the increment
``g = L̂_j`` satisfies, for each scale ``x ∈ {N, D}``:

(i)   ``∂g/∂x ≤ −∂L̂^{(j−1)}/∂x`` for all ``x ≥ x_min``
(ii)  ``∂²g/∂x² ≥ −∂²L̂^{(j−1)}/∂x²`` for all ``x ≥ x_min``
(iii) ``g(h) > −L̂^{(j−1)}(h)`` for all ``h ∈ ℍ``
(iv)  ``L̂^{(j−1)}(h) + g(h) > L_∞`` for all ``h ∈ ℍ``
(v)   ``g(h)|_{x=t} = O(t^{c_{x,j}})`` as ``t → ∞`` for some
      ``c_{x,j} < c_x^{(0)}`` (equivalently ``ord(g, x) < c_x^{(0)}``)
(vi)  ``g ∈ C^∞`` on ``[x_min, x_max]`` with ``|g(x_min, ·)| < ∞``

Conditions (i)–(iv), (vi) on the compact box are handled by sound interval
certificates; (v) by the structural exponent ``ord(g, x)``
(see ``src.certificates``).
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class StageAdmissibilityVerdict:
    """Outcome of checking (i)–(vi) for a candidate increment ``g``."""

    accepted: bool
    details: dict[str, Any]


class StageAdmissibilityChecker(ABC):
    """Decide whether ``g`` preserves admissibility of the ensemble."""

    @abstractmethod
    def check(
        self,
        candidate: Any,
        ensemble_state: Any,
        *args: Any,
        **kwargs: Any,
    ) -> StageAdmissibilityVerdict:
        """
        Parameters
        ----------
        candidate:
            Expression tree / program ``g`` (representation is student-defined).
        ensemble_state:
            Enough information to evaluate ``L̂^{(j−1)}`` and its IA image
            (floors, prior programs, domains ``I_x``, exponents ``c_x^{(0)}``, …).
        """
