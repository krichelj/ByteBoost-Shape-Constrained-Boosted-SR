"""
Decoder-only transformer stub (``sec:models``).

Build a compact post-LN causal LM matching ``ModelConfig``.
Workshop ports may swap in LLaMA-style blocks, FlashAttention, or μP;
the method only requires consistent ``(N, D, L)`` measurements.
"""

from __future__ import annotations

from typing import Any

from src.modeling.models.config import ModelConfig


class CausalTransformerLM:
    """Decoder-only language model used to produce validation losses ``L(h)``."""

    def __init__(self, config: ModelConfig):
        self.config = config
        raise NotImplementedError("TODO: embedding + transformer blocks + LM head")

    def forward(self, input_ids: Any, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError("TODO: causal LM forward (manual mask or FA)")

    def num_parameters(self) -> int:
        raise NotImplementedError("TODO: return N")
