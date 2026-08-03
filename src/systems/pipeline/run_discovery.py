"""
End-to-end discovery pipeline and deliverable hooks (``sec:deliverables``).

Deliverables
------------
(1) An admissible boosted scaling law (``sec:axioms``, ``sec:guarantee``) fit on
    the collected training grid (``sec:datasets``).
(2) Public release of the shape-constrained SR library with IA-certified
    admissibility checking (``sec:certificates``).
(3) A short paper / methods report on ``sec:method``.

This module wires student implementations into a single runnable entry point.
Default ``DiscoveryConfig.path`` is ``\"soft\"`` (primary gplearn + IA penalties);
set ``path=\"hard\"`` for the workshop reject-filter extension.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


SearchPath = Literal["soft", "hard"]


@dataclass
class DiscoveryConfig:
    """Top-level knobs for a discovery run (concrete fields are student-defined)."""

    num_stages: int  # K
    path: SearchPath = "soft"
    # baseline_name: str = "chinchilla"
    # data_uri: str = ...
    # lambdas: dict[str, float] | None = None


@dataclass
class DiscoveryResult:
    """Artifacts for deliverable (1)."""

    expression: str
    joint_floor: float
    exponents: dict[str, float]
    metrics: dict[str, Any]
    guarantee_ok: bool


def run_discovery(config: DiscoveryConfig, *args: Any, **kwargs: Any) -> DiscoveryResult:
    """Load ``D``, run Algorithm 1 (``sec:algorithm``), verify guarantee, return artifacts.

    Typical soft-path wiring
    ------------------------
    setup → stage-0 NLS baseline → for each stage: Huber residuals → soft
    ``F_j`` search → ensemble update → guarantee / soft ``V`` report.
    """
    raise NotImplementedError(
        "TODO: wire setup → baseline → soft (or hard) boosting → guarantee.check"
    )


def export_library_api() -> dict[str, Any]:
    """Enumerate public symbols intended for deliverable (2) (documentation aid)."""
    raise NotImplementedError("TODO: list stable imports for the open-source release")
