"""
Pretraining corpora named in ``sec:datasets``.

Wikipedia, RedPajama, FineWeb-Edu — used when generating new ``(N, D, L)``
points on Neocortex / GPU baselines. Tokenization and packing details are
left to students / site-specific storage layouts.
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
    def documents(self) -> Iterator[str]:
        raise NotImplementedError("TODO: stream FineWeb-Edu shards")


def pretokenize(corpus: Corpus, *args: Any, **kwargs: Any) -> Any:
    """Optional offline tokenization step for pretraining corpora."""
    raise NotImplementedError("TODO: tokenize / pack sequences for training")
