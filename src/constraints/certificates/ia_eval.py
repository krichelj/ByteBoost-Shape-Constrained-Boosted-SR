"""
Tree evaluation under DualInterval and structural asymptotic checks
(``sec:certificates``, certificate (b)).

Structural checks
-----------------
* ``ord(g, x)`` — asymptotic exponent of expression tree ``g`` along scale ``x``,
  defined recursively: non-``x`` leaves → 0; ``pow_p(x)`` → ``p``; products add;
  quotients subtract; sums take the maximum.
* Stage condition (v) holds with ``c_{x,j} = ord(g, x)`` when
  ``ord(g, x) < c_x^{(0)}`` for each ``x ∈ {N, D}``.
* Each scale leaf ``x ∈ {N, D}`` must appear in ``leaves(g)`` (else the
  exponent in ``x`` is undefined / vacuously 0).

IA evaluation
-------------
Walk the finite expression tree bottom-up on DualInterval operands
(operators ``{+, ×, ÷} ∪ {pow_p : p ∈ P}``).
"""

from __future__ import annotations

from typing import Any, Iterable, Sequence

from src.constraints.certificates.interval import DualInterval


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
