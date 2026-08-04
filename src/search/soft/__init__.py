"""
Shape-constrained soft search (``sec:soft``, Prop. 3 / ``prop:soft``).

Sole discovery package for Algorithm 1: gplearn (optional PySR ablation) with
DualInterval axiom penalties on compact slices ``I_x ⊂ ℍ̃``, folded into
fitness ``F_j`` (eq. penalized-bb). Soft scores ``v_a`` come from IA /
structural enclosures as continuous gaps. When ``V = 0`` with finite
DualInterval enclosures, certificates (a)–(b) hold and the boosting guarantee
applies (A5 via ``v_irred``; A6 via finiteness / ``C^∞`` operators, not a
separate soft score).

There is no hard reject-filter package; do not add one.

See ``violations.py``, ``fitness.py``, ``backends.py``.
"""
