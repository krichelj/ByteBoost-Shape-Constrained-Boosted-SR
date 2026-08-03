"""
HPC profiling hooks (``sec:testbeds``, ``sec:baselines``, ``sec:collaborators``).

Search track: port the GP + IA certification inner loop to AMA27
(AmpereOne A192-32M) and compare against AMD EPYC (x86) CPU baselines.
The workload is population-parallel and largely scalar — useful AMA27
properties are Arm ISA diversity, high core counts, and dense node count.

Modeling track: compare Cerebras CS-3 pretraining throughput / loss curves
to NVIDIA GH200 baselines.
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
    """Benchmark one boosting stage's SR search on the current host."""
    raise NotImplementedError("TODO: end-to-end stage timing on AMA27 vs EPYC")


def compare_pretrain_platforms(
    neocortex_metrics: dict[str, Any],
    gpu_metrics: dict[str, Any],
) -> dict[str, Any]:
    """Summarize CS-3 vs GH200 pretraining comparisons for the methods report."""
    raise NotImplementedError("TODO: normalize and compare loss / throughput")
