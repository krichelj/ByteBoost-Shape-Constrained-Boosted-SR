"""
Tree evaluation under DualInterval and structural asymptotic checks
(``sec:certificates``).

Helpers for both certificate (a) (IA enclosures of ``F``, ``∂F/∂x``, ``∂²F/∂x²``
on a compact slice of ``ℍ̃``) and certificate (b) (structural ``ord`` / leaf
checks for the ``x → ∞`` tail beyond ``I_x``). Soft scores (``sec:soft``)
reuse the same routines.

Search features are typically ``log φ_h(h)`` for every coordinate
``h ∈ {N, D} ∪ H``. Evaluate DualIntervals in that coordinate system, then map
first/second derivatives to the raw scale axis via ``chain_rule_log_to_raw``
before applying the interval tests of eq. interval-bb (raw-axis (A1)–(A2)).

Structural checks (certificate (b))
-----------------------------------
* ``ord(g, x)`` — asymptotic exponent of expression tree ``g`` along scale ``x``,
  defined recursively: non-``x`` leaves → 0; ``pow_p(x)`` → ``p``; products add;
  quotients subtract; sums take the maximum.
  Decay scoring must compare against ``c_x^{(0)}`` (do not drop the stage-0 rate).
* Stage condition (v) holds with ``c_{x,j} = ord(g, x)`` when
  ``ord(g, x) < c_x^{(0)}`` for each ``x ∈ {N, D}``.
* Each scale leaf ``x ∈ {N, D}`` must appear in ``leaves(g)``.

IA evaluation (certificate (a) substrate)
-----------------------------------------
Walk the finite expression tree bottom-up on DualInterval operands with the
same primary operator set as search (``sec:boosting``):

    ``{+, −, ×, ÷} ∪ {pow_p : p ∈ P}``

These primitives are ``C^∞`` on ``(0, ∞)``, which discharges graceful
saturation (A5) on ``I_x`` once ``F̄ < ∞``. Optional unary helpers
``inv`` / ``log`` / ``sqrt`` may be enabled for ablations.
"""

from __future__ import annotations

from typing import Any, Iterable, Sequence

from src.constraints.certificates.interval import DualInterval, Interval


def evaluate_program(
    program: Sequence[Any],
    intervals: dict[int, DualInterval],
) -> DualInterval:
    """Evaluate expression tree ``program`` under DualInterval feature map.

    Parameters
    ----------
    program:
        Student-defined tree encoding (e.g. gplearn prefix list).
    intervals:
        Map from feature index → DualInterval operand on the relevant
        ``I_x`` / frozen ``H_h`` ranges (slice of ``ℍ̃``).
    """
    raise NotImplementedError("TODO: recursive DualInterval evaluation of program")


def asymptotic_exponent(program: Sequence[Any], var_index: int) -> float:
    """Compute ``ord(g, x)`` for the scale feature at ``var_index``."""
    raise NotImplementedError("TODO: structural walk implementing ord(g, x)")


def leaves(program: Sequence[Any]) -> set[int]:
    """Return ``leaves(g)`` as the set of variable feature indices in ``g``."""
    raise NotImplementedError("TODO: collect variable leaves of the tree")


def check_scale_leaves(
    program: Sequence[Any],
    required_indices: Iterable[int],
) -> float:
    """Soft leaf score: count how many required scale indices are missing.

    Used as ``v_leaf(g) = |{x ∈ {N,D} : x ∉ leaves(g)}|`` in soft search.
    """
    raise NotImplementedError("TODO: compare leaves(program) to required_indices")


def chain_rule_log_to_raw(
    f_log: DualInterval,
    x_raw: Interval,
) -> DualInterval:
    """Map DualInterval derivatives from ``u = log x`` back to raw ``x``.

    If search features are ``log φ_h(h)``, IA evaluates ``(f, ∂f/∂u, ∂²f/∂u²)``.
    Raw-axis certificates (A1)–(A2) need ``∂f/∂x = (∂f/∂u)/x`` and
    ``∂²f/∂x² = (∂²f/∂u² − ∂f/∂u)/x²`` (enclose each term with DualInterval).
    """
    raise NotImplementedError("TODO: implement log→raw DualInterval chain rule")
