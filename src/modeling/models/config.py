"""
Decoder-only LM configuration (``sec:models``).

Core target: a compact post-LN causal transformer stack suitable for scaling
grids, spanning roughly ``10M–1.4B`` parameters across several
tokens-per-parameter ratios ``M = D/N``, in the Step Law / overtraining
regimes. Workshop ports may adopt LLaMA-style blocks, FlashAttention, and
``μP`` / ``μTransfer`` to decouple optimization from scale; the method only
requires consistent ``(N, D, L)`` measurements.

Concrete layer widths, depths, and vocab size are student/experiment choices.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ModelConfig:
    """Architectural hyperparameters for a single grid point."""

    n_layers: int
    n_heads: int
    d_model: int
    vocab_size: int
    # Optional μP / other fields:
    # mup_base_width: int | None = None

    def total_params(self) -> int:
        """Return parameter count ``N`` (exclude embeddings if that is your convention)."""
        raise NotImplementedError("TODO: count parameters consistently with the grid")

    def tokens_for_ratio(self, m: float) -> int:
        """Return token budget ``D = M · N`` for tokens-per-parameter ratio ``M = m``."""
        raise NotImplementedError("TODO: D = m * N")
