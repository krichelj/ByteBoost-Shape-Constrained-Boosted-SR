"""
Boosting guarantee (``sec:guarantee``, Thm. 1 / ``thm:guarantee``, eq. guarantee-bb).

The sole discovery method (``sec:soft``) drives each correction toward
``V = 0`` with finite DualInterval enclosures. When that holds at every stage
(``prop:soft``), certificates (a)–(b) are satisfied and for all ``j``:

* ``L̂^{(j)} ∈ S`` on ``ℍ̃`` (A1–A6);
* writing ``L_∞^{(j)}`` for the joint floor of ``L̂^{(j)}``, one has
  ``L_∞^{(j)} = E``;
* asymptotic exponents are preserved:

    lim_{t→∞} log(L̂^{(j)}(h)|_{x=t} − L^∞_x) / log t  =  c_x^{(0)},

  where ``L^∞_x`` is the marginal floor of ``L̂^{(j)}`` along ``x``
  (depends on frozen coordinates; equal to that of ``L̂_0``).

Here ``v_irred = 0`` covers both the joint floor and positivity (A5); A6 is
discharged by successful finite IA under the ``C^∞`` operator set. Boosting
therefore improves fit *without* corrupting the interpretable constants
researchers quote. Implement empirical checks / unit tests that probe these
invariants on fitted ensembles.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class GuaranteeReport:
    """Empirical / certified status of the ``sec:guarantee`` invariants."""

    admissible: bool
    joint_floor_preserved: bool
    exponents_preserved: dict[str, bool]
    details: dict[str, Any]


def verify_guarantee(
    ensemble: Any,
    stage0: Any,
    *args: Any,
    **kwargs: Any,
) -> GuaranteeReport:
    """Check floor / exponent preservation relative to stage 0.

    Parameters
    ----------
    ensemble:
        Fitted ``L̂^{(K)}`` (or intermediate ``L̂^{(j)}``).
    stage0:
        Baseline providing ``E`` and ``c_x^{(0)}``.
    """
    raise NotImplementedError(
        "TODO: compare L_∞^{(j)} to E and measured/structural c_x to c_x^{(0)}"
    )
