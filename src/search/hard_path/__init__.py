"""
Hard search path (``sec:stage-admiss``, workshop extension).

Optional reject filter: discard candidates that fail certificates (a)–(b)
during GP search. The primary shipped method is soft-penalty search
(``src.search.soft_path``, ``sec:soft``); implement this path on the same
DualInterval helpers.

See ``search.py``.
"""
