"""
LLaMA-style decoder-only transformer stub (``sec:models``).

Software stack (``sec:software``): PyTorch 2.x with FlashAttention for
pretraining. Build a minimal decoder block stack matching ``ModelConfig``.
"""

from __future__ import annotations

from typing import Any

from src.models.config import ModelConfig


class LlamaLikeLM:
    """Decoder-only language model used to produce validation losses ``L(h)``."""

    def __init__(self, config: ModelConfig):
        self.config = config
        # TODO: construct embedding + transformer blocks + head
        raise NotImplementedError("TODO: construct embedding + transformer blocks + head")

    def forward(self, input_ids: Any, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("TODO: causal LM forward")

    def num_parameters(self) -> int:
        raise NotImplementedError("TODO: return N")
