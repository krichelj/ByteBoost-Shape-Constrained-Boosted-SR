"""Falsifiable tests for scaling setup constants (sec:setup, sec:soft)."""

from __future__ import annotations

from src.scaling.setup.constants import (
    AXIOM_INDICES,
    DEFAULT_LAMBDAS,
    EPSILON_DECAY,
    SCALE_VARS,
)


def test_scale_variables_match_spec() -> None:
    """Axiomatic scale variables must be exactly ('N', 'D')."""
    assert SCALE_VARS == ("N", "D")
    assert len(SCALE_VARS) == 2


def test_axiom_indices_correspondence() -> None:
    """Soft search axiom indices must cover A1-A4 plus leaf prerequisite."""
    expected = ("mono", "conv", "irred", "decay", "leaf")
    assert expected == AXIOM_INDICES


def test_epsilon_decay_positivity() -> None:
    """EPSILON_DECAY must be strictly positive to ensure strict power-law inequality."""
    assert EPSILON_DECAY > 0.0
    assert isinstance(EPSILON_DECAY, float)


def test_default_lambdas_cover_all_axioms() -> None:
    """DEFAULT_LAMBDAS must define positive weights for each axiom index."""
    for axiom in AXIOM_INDICES:
        assert axiom in DEFAULT_LAMBDAS, f"Missing penalty weight for axiom {axiom}"
        assert DEFAULT_LAMBDAS[axiom] > 0.0, f"Weight for {axiom} must be strictly positive"


def test_default_lambdas_no_extraneous_keys() -> None:
    """Negative control: DEFAULT_LAMBDAS must not contain undocumented axiom weights."""
    extra_keys = set(DEFAULT_LAMBDAS.keys()) - set(AXIOM_INDICES)
    assert not extra_keys, f"Unexpected penalty keys: {extra_keys}"
