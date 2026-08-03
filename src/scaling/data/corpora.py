"""
Pretraining corpora named in ``sec:datasets``.

Primary mixtures: Wikipedia, RedPajama, and related open text — used when
generating new ``(N, D, L)`` points on Neocortex / GPU baselines.
FineWeb-Edu is an optional workshop extension (not required for the core grid).

Tokenization and packing details are left to students / site-specific storage.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterator


class Corpus(ABC):
    """Streaming / sharded text corpus for LM pretraining."""

    @abstractmethod
    def documents(self) -> Iterator[str]:
        """Yield raw documents."""


class WikipediaCorpus(Corpus):
    def documents(self) -> Iterator[str]:
        raise NotImplementedError("TODO: stream Wikipedia dump / subset")


class RedPajamaCorpus(Corpus):
    def documents(self) -> Iterator[str]:
        raise NotImplementedError("TODO: stream RedPajama shards")


class FineWebEduCorpus(Corpus):
    """Optional workshop-extension corpus (``sec:datasets``)."""

    def documents(self) -> Iterator[str]:
        raise NotImplementedError("TODO: stream FineWeb-Edu shards (optional)")


def pretokenize(corpus: Corpus, *args: Any, **kwargs: Any) -> Any:
    """Optional offline tokenization step for pretraining corpora."""
    raise NotImplementedError("TODO: tokenize / pack sequences for training")
