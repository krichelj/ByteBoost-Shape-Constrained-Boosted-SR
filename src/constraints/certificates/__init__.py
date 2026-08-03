"""
Interval / DualInterval certificates and tree evaluation (``sec:certificates``).

Shared by soft scores and the hard reject filter: ``interval.py`` (arithmetic),
``ia_eval.py`` (tree walk, ``ord``, log→raw chain rule),
``hard_certificates.py`` (eq. interval-bb accept test / enclosures),
``jax_backend.py`` (optional JAX+JVP acceleration).
"""
