"""
Configuration space and labeled dataset (project description ``sec:setup``).

Formal objects
--------------
* ``N``, ``D`` — scale variables (parameter count, training-token count).
* ``H = {h_1, …, h_m}`` — remaining hyperparameters.
* For each coordinate ``h ∈ {N, D} ∪ H``, a finite admissible set ``H_h`` and a
  strictly monotone preprocessing map ``φ_h : H_h → R_{>0}``.
* Configuration space ``ℍ = ∏_h H_h`` with typical element ``h ∈ ℍ``.
* Continuum domain ``ℍ̃`` for admissibility (``sec:axioms``): each scale ranges
  over ``[x_min, ∞)``, other coordinates over finite ``H_h``; ``ℍ ⊂ ℍ̃``.
* Validation loss ``L : ℍ → R``; approximation ``L̂ ≈ L`` (extended along scales
  to ``ℍ̃`` when stating A1–A5).
* Labeled dataset ``D = {(h_ℓ, L(h_ℓ))}_{ℓ=1}^n ⊂ ℍ × R``.
* For each scale ``x ∈ {N, D}``: ``x_min = min H_x > 0``, ``x_max = max H_x``;
  treat ``x`` as continuous on ``[x_min, ∞)``.
* GP / symbolic features are typically ``log φ_h(h)`` for every coordinate
  ``h ∈ {N, D} ∪ H`` (chain rule maps log-axis derivatives back to raw
  ``N``, ``D`` before scoring axioms A1–A2).

Students choose concrete dtypes / containers (e.g. ``numpy`` arrays, column
maps). Keep the mathematical roles intact.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable, Mapping, Sequence


# Type aliases — refine as needed (arrays, tensors, …).
ConfigPoint = Any  # element h ∈ ℍ (or continuum point in ℍ̃ for axiom checks)
LossValue = float
PreprocessMap = Callable[[Any], float]  # φ_h


@dataclass
class CoordinateSpec:
    """Specification of one coordinate ``h`` of ``ℍ``.

    Attributes
    ----------
    name:
        Coordinate name (e.g. ``\"N\"``, ``\"D\"``, or a hyperparameter id).
    admissible_values:
        Finite set ``H_h``. Representation is up to you (list, array, …).
    phi:
        Strictly monotone preprocessing ``φ_h : H_h → R_{>0}``.
    is_scale:
        True iff this coordinate is a scale variable ``x ∈ {N, D}``.
    """

    name: str
    admissible_values: Sequence[Any]
    phi: PreprocessMap
    is_scale: bool = False

    @property
    def x_min(self) -> float:
        """``x_min = min H_x`` for scale coordinates; raise if non-scale."""
        raise NotImplementedError("TODO: return min of admissible_values as float")

    @property
    def x_max(self) -> float:
        """``x_max = max H_x`` for scale coordinates; raise if non-scale."""
        raise NotImplementedError("TODO: return max of admissible_values as float")


@dataclass
class ConfigurationSpace:
    """Product space ``ℍ = ∏_h H_h`` (``sec:setup``).

    Also defines the continuum domain ``ℍ̃`` used by A1–A5: scale coordinates
    extend to ``[x_min, ∞)`` while non-scale coordinates stay on finite ``H_h``.
    Certification boxes ``I_x = [x_min, x_max]`` are compact slices of ``ℍ̃``.
    """

    coordinates: Mapping[str, CoordinateSpec] = field(default_factory=dict)

    def scale_coords(self) -> Iterable[CoordinateSpec]:
        """Yield coordinates with ``x ∈ {N, D}``."""
        raise NotImplementedError("TODO: filter is_scale coordinates")

    def hyperparameter_coords(self) -> Iterable[CoordinateSpec]:
        """Yield coordinates in ``H = {h_1, …, h_m}``."""
        raise NotImplementedError("TODO: filter non-scale coordinates")

    def certification_domains(self) -> dict[str, Any]:
        """Return IA domains for each scale box ``I_x`` and frozen ``H_h`` ranges.

        Used by DualInterval certificates (``sec:certificates``) as a compact
        continuum slice of ``ℍ̃`` covering the observed grid.
        """
        raise NotImplementedError("TODO: build Interval domains for I_x and H_h")

    def preprocess(self, h: ConfigPoint) -> Any:
        """Apply ``φ`` coordinate-wise to a configuration ``h ∈ ℍ``.

        Return type is student-defined (feature vector for SR, etc.).
        """
        raise NotImplementedError("TODO: apply each CoordinateSpec.phi")


@dataclass
class LabeledDataset:
    """Labeled dataset ``D = {(h_ℓ, L(h_ℓ))}_{ℓ=1}^n`` (``sec:setup``)."""

    space: ConfigurationSpace
    points: Sequence[ConfigPoint]
    losses: Sequence[LossValue]

    def __len__(self) -> int:
        """Cardinality ``n = |D|``."""
        raise NotImplementedError("TODO: return number of labeled pairs")

    def as_arrays(self) -> tuple[Any, Any]:
        """Materialize design matrix / response for fitting.

        Returns
        -------
        X, y :
            Student-defined arrays with rows corresponding to ``ℓ = 1…n``.
        """
        raise NotImplementedError("TODO: stack configurations and losses")


class DatasetLoader(ABC):
    """Load ``D`` from disk, Hugging Face, or an experiment inventory."""

    @abstractmethod
    def load(self, *args: Any, **kwargs: Any) -> LabeledDataset:
        """Return a labeled scaling dataset (see also ``src.scaling.data``)."""
