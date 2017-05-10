# Copyright (c) 2017 Oleg Bulkin
# MIT License (https://opensource.org/licenses/MIT)

# Try to import public functions from the C extension module, falling back to
# the Python implementation as needed. This allows library users to import from
# stringdist without worrying about which implementation was selected
try:
    from cstringdist import (levenshtein, levenshtein_norm, rdlevenshtein,
                             rdlevenshtein_norm)
except ImportError:
    from .pystringdist import (levenshtein, levenshtein_norm, rdlevenshtein,
                               rdlevenshtein_norm)
