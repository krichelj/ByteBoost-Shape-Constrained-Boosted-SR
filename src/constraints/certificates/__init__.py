"""
Interval / DualInterval certificates and tree evaluation (``sec:certificates``).

Soft search (``sec:soft``, ``src.search.soft``) uses these primitives as the
substrate for continuum violation scores on compact slices of ``ℍ̃`` (``I_x``
boxes) plus structural ``ord`` for the ``x→∞`` tail:

* ``interval.py`` — arithmetic / DualInterval (needs ``d2`` for A2)
* ``ia_eval.py`` — tree walk, ``ord``, log→raw chain rule
* ``ia_certificates.py`` — eq. interval-bb enclosures (input to ``v_a``)
* ``jax_backend.py`` — optional JAX+JVP acceleration

Enclosures feed soft scores; they are not a search-time reject filter.
"""
