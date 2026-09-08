"""Contract tests for Interval and DualInterval arithmetic (sec:certificates)."""

from __future__ import annotations

import pytest

from src.constraints.certificates.interval import DualInterval, Interval


def test_interval_instantiation_raises_not_implemented() -> None:
    """Interval.__post_init__ raises NotImplementedError until student validation is implemented."""
    with pytest.raises(NotImplementedError) as exc_info:
        Interval(lo=1.0, hi=2.0)
    assert "TODO: validate lo" in str(exc_info.value)


def test_dual_interval_static_constructors_raise_not_implemented() -> None:
    """DualInterval helper constructors raise NotImplementedError until implemented."""
    with pytest.raises(NotImplementedError):
        DualInterval.constant(1.0)

    with pytest.raises(NotImplementedError):
        # We pass dummy intervals assuming mock or stub
        DualInterval.variable(Interval.__new__(Interval))

    with pytest.raises(NotImplementedError):
        DualInterval.parameter(Interval.__new__(Interval))
