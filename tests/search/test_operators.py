"""Falsifiable tests for symbolic regression primitive operators (sec:boosting)."""

from __future__ import annotations

import pytest

from src.search.expression.operators import (
    DEFAULT_POWERS,
    default_function_set,
    make_power_primitives,
)


def test_default_powers_exclude_zero() -> None:
    """The admissible power set P must be a subset of R \\ {0}."""
    assert 0.0 not in DEFAULT_POWERS
    for p in DEFAULT_POWERS:
        assert p != 0.0, "Zero exponent is not an admissible power-law correction"


def test_default_powers_span_positive_and_negative() -> None:
    """Powers must include negative exponents (decay) and positive exponents."""
    negatives = [p for p in DEFAULT_POWERS if p < 0.0]
    positives = [p for p in DEFAULT_POWERS if p > 0.0]
    assert len(negatives) > 0, "Admissible powers must include negative exponents"
    assert len(positives) > 0, "Admissible powers must include positive exponents"


def test_default_powers_include_fractional_powers() -> None:
    """Powers must include fractional exponents for non-integer scaling behavior."""
    fractionals = [p for p in DEFAULT_POWERS if not p.is_integer()]
    assert len(fractionals) > 0, "Admissible powers must include fractional exponents"


def test_operator_stubs_raise_not_implemented() -> None:
    """Operator generator stubs must raise NotImplementedError until students implement them."""
    with pytest.raises(NotImplementedError):
        make_power_primitives()
    with pytest.raises(NotImplementedError):
        default_function_set()
