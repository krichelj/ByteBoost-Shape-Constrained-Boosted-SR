"""
HPC profiling hooks (``sec:testbeds``, ``sec:collaborators``).

Search track: port the GP + IA certification inner loop to AMA27
(AmpereOne A192-32M). The workload is population-parallel and largely scalar, so the
useful AMA27 properties are Arm ISA diversity, high core counts, and dense
node count for concurrent candidate evaluation.

Modeling track: profile Cerebras CS-3 / Neocortex pretraining throughput on the
requested testbed. Loss-level comparison to existing public HF scaling curves
belongs in ``src.scaling.data`` / ``sec:baselines`` (not a hardware baseline).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class ProfileResult:
    """Timing / scaling measurement for a workload fragment."""

    label: str
    wall_seconds: float
    extras: dict[str, Any]


def profile_callable(label: str, fn: Callable[[], Any]) -> ProfileResult:
    """Time ``fn()`` and return a ``ProfileResult``."""
    raise NotImplementedError("TODO: wall-clock profile helper")


def profile_certification_inner_loop(*args: Any, **kwargs: Any) -> ProfileResult:
    """Benchmark IA certificate evaluation over a candidate population."""
    raise NotImplementedError("TODO: microbenchmark DualInterval certificates")


def profile_stage_search(*args: Any, **kwargs: Any) -> ProfileResult:
    """Benchmark one boosting stage's SR search on the current host (e.g. AMA27)."""
    raise NotImplementedError("TODO: end-to-end stage timing on AMA27")


def summarize_neocortex_pretrain(metrics: dict[str, Any]) -> dict[str, Any]:
    """Summarize Neocortex CS-3 pretraining throughput / run metadata for the report."""
    raise NotImplementedError("TODO: normalize Neocortex throughput / wall-time metrics")
