"""
Primary soft search path (``sec:soft``, Prop. 3 / ``prop:soft``).

Default discovery path: gplearn (optional PySR ablation) with DualInterval
axiom penalties on compact slices ``I_x ⊂ ℍ̃``, folded into fitness ``F_j``
(eq. penalized-bb). Soft scores ``v_a`` come from the same IA/structural
certificates as the hard filter, but as continuous gaps rather than a reject
gate. ``V = 0`` plus finite DualInterval enclosures recovers admissibility on
``ℍ̃`` (A5 via ``v_irred``; A6 via finiteness / ``C^∞`` operators, not a
separate soft score).

See ``violations.py``, ``fitness.py``, ``backends.py``.
"""
