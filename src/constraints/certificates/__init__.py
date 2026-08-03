"""
Interval / DualInterval certificates and tree evaluation (``sec:certificates``).

Shared by soft scores and the hard reject filter. Certify continuum conditions
on compact slices of ``ℍ̃`` (``I_x`` boxes) plus structural ``ord`` for the
``x→∞`` tail:

* ``interval.py`` — arithmetic / DualInterval (needs ``d2`` for A2)
* ``ia_eval.py`` — tree walk, ``ord``, log→raw chain rule
* ``hard_certificates.py`` — eq. interval-bb accept test / enclosures
  (A1–A3/A5/A6 on the box)
* ``jax_backend.py`` — optional JAX+JVP acceleration
"""
