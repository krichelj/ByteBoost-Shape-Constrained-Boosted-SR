"""
Scaling-law datasets (``sec:datasets``, ``sec:setup``, ``sec:baselines``).

Sources named in the project description:
* Wikipedia, RedPajama, and related open text mixtures — pretraining corpora
  (modeling track). FineWeb-Edu is an *optional* workshop extension.
* Public ``colinear_scaling_models`` on Hugging Face — trained checkpoints and
  validation-loss curves (``sec:baselines``). Compare *losses* with new
  Neocortex runs; the original training hardware is out of scope and not
  available to students.

This module concerns the *labeled* pairs ``(h_ℓ, L(h_ℓ))`` that feed symbolic
regression and loss-level baseline comparison. Corpus download/tokenization
lives under ``src.modeling.training`` / ``corpora.py``.
"""

from __future__ import annotations

from typing import Any

from src.scaling.setup.configuration import DatasetLoader, LabeledDataset


class HuggingFaceScalingLoader(DatasetLoader):
    """Load loss curves / checkpoint metadata from the public colinear collection.

    Workshop baseline for ``sec:baselines``: build ``D = {(h_ℓ, L(h_ℓ))}`` from
    published losses; do not assume access to the original training cluster.
    """

    def load(self, *args: Any, **kwargs: Any) -> LabeledDataset:
        raise NotImplementedError(
            "TODO: fetch HF dataset leibnitz-lab/colinear_scaling_models "
            "(or successor) and build D = {(h_ℓ, L(h_ℓ))}"
        )


class TabularScalingLoader(DatasetLoader):
    """Load a local spreadsheet / CSV of ``(N, D, …, L)`` rows."""

    def load(self, *args: Any, **kwargs: Any) -> LabeledDataset:
        raise NotImplementedError("TODO: parse tabular scaling inventory into LabeledDataset")


def train_holdout_split(
    dataset: LabeledDataset,
    *args: Any,
    **kwargs: Any,
) -> tuple[LabeledDataset, LabeledDataset]:
    """Split ``D`` into fit / extrapolation or holdout folds (student-defined)."""
    raise NotImplementedError("TODO: define interpolation vs extrapolation splits")


def compare_loss_curves(
    neocortex_losses: Any,
    baseline_losses: Any,
    *args: Any,
    **kwargs: Any,
) -> dict[str, Any]:
    """Compare new Neocortex ``L(h)`` values to public HF baseline losses (``sec:baselines``)."""
    raise NotImplementedError("TODO: align grids and summarize loss-level differences")
