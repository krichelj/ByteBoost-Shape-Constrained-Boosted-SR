"""
Huber clipping threshold ``δ_j`` and pseudo-residuals ``r̃_j`` (``sec:boosting``,
eq. delta-bb, eq. pseudoresid-bb).

Stage ``j ≥ 1`` of Algorithm 1 fits corrections to these robust targets so
outlier runs cannot dominate the stage MSE.

See ``huber.py``.
"""
