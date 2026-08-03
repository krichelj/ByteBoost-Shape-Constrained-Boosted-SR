"""
Tree evaluation under DualInterval and structural asymptotic checks
(``sec:certificates``, certificate (b)).

Search features are typically ``log φ_h(h)``. Evaluate DualIntervals in that
coordinate system, then map first/second derivatives to the raw scale axis via
``chain_rule_log_to_raw`` before applying the interval tests of eq. interval.

Structural checks
-----------------
* ``ord(g, x)`` — asymptotic exponent of expression tree ``g`` along scale ``x``,
  defined recursively: non-``x`` leaves → 0; ``pow_p(x)`` → ``p``; products add;
  quotients subtract; sums take the maximum.
  Decay scoring must compare against ``c_x^{(0)}`` (do not drop the stage-0 rate).
* Stage condition (v) holds with ``c_{x,j} = ord(g, x)`` when
  ``ord(g, x) < c_x^{(0)}`` for each ``x ∈ {N, D}``.
* Each scale leaf ``x ∈ {N, D}`` must appear in ``leaves(g)``.

IA evaluation
-------------
Walk the finite expression tree bottom-up on DualInterval operands
(operators ``{+, ×, ÷} ∪ {pow_p : p ∈ P}``; optional neg/inv for ablations).
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
        Map from feature index → DualInterval operand.
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
    """Soft/hard leaf score: count how many required scale indices are missing.

    Used as ``v_leaf(g) = |{x ∈ {N,D} : x ∉ leaves(g)}|`` on the soft path.
    """
    raise NotImplementedError("TODO: compare leaves(program) to required_indices")


def chain_rule_log_to_raw(
    f_log: DualInterval,
    x_raw: Interval,
) -> DualInterval:
    """Map DualInterval derivatives from ``u = log x`` back to raw ``x``.

    If search features are ``log φ_h(h)``, IA evaluates ``(f, ∂f/∂u, ∂²f/∂u²)``.
    Raw-axis certificates need ``∂f/∂x = (∂f/∂u)/x`` and
    ``∂²f/∂x² = (∂²f/∂u² − ∂f/∂u)/x²`` (enclose each term with DualInterval).
    """
    raise NotImplementedError("TODO: implement log→raw DualInterval chain rule")
