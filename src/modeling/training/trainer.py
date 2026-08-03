"""
Pretraining loop stubs (modeling track; ``sec:testbeds``, ``sec:software``).

Neocortex (PSC) Cerebras CS-3 systems are requested for the pretraining grid;
compare loss curves to existing NVIDIA GH200 baselines (DeltaAI / local).
Environment: ``uv``, Weights & Biases logging.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from src.modeling.models.config import ModelConfig


class PretrainTrainer(ABC):
    """Train a decoder-only LM and record validation loss for the scaling grid."""

    @abstractmethod
    def train(
        self,
        config: ModelConfig,
        token_budget: int,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """
        Returns
        -------
        metrics :
            Must include validation loss ``L`` and identifiers for ``N``, ``D``, …
            suitable for appending to ``D``.
        """


class TorchPretrainTrainer(PretrainTrainer):
    """PyTorch DDP path (GPU baselines / portable prototype).

    FlashAttention / μP / LLaMA-style blocks are optional ports — not required
    for a consistent ``(N, D, L)`` measurement grid.
    """

    def train(
        self,
        config: ModelConfig,
        token_budget: int,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        raise NotImplementedError("TODO: PyTorch training loop + W&B logging")


class NeocortexPretrainTrainer(PretrainTrainer):
    """Cerebras CS-3 / Neocortex port (``sec:testbeds``)."""

    def train(
        self,
        config: ModelConfig,
        token_budget: int,
        *args: Any,
        **kwargs: Any,
    ) -> dict[str, Any]:
        raise NotImplementedError(
            "TODO: port pretraining to Neocortex CS-3; emit comparable loss curves"
        )
