"""
Primary soft search path (``sec:soft``, Prop. 3 / ``prop:soft``).

Default discovery path: gplearn (optional PySR ablation) with DualInterval
axiom penalties folded into fitness ``F_j`` (eq. penalized-bb). Soft scores
``v_a`` come from the same IA/structural certificates as the hard filter, but
as continuous gaps rather than a reject gate.

See ``violations.py``, ``fitness.py``, ``backends.py``.
"""
