"""
Scaling-law datasets (``sec:datasets``, ``sec:setup``).

Sources named in the project description:
* Wikipedia, RedPajama, and related open text mixtures — pretraining corpora
  (modeling track). FineWeb-Edu is an *optional* workshop extension.
* Public ``colinear_scaling_models`` on Hugging Face — trained checkpoints and
  loss curves from an initial DeltaAI grid (already available).

This module concerns the *labeled* pairs ``(h_ℓ, L(h_ℓ))`` that feed symbolic
regression. Corpus download/tokenization lives under ``src.modeling.training`` /
``corpora.py``.
"""

from __future__ import annotations

from typing import Any

from src.scaling.setup.configuration import DatasetLoader, LabeledDataset


class HuggingFaceScalingLoader(DatasetLoader):
    """Load loss curves from the public colinear scaling collection."""

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
