# Copyright (c) 2017 Oleg Bulkin
# MIT License (https://opensource.org/licenses/MIT)

# Import shared helper
from .levenshtein_shared import _levenshtein_compute


def levenshtein(source, target):
    """Calculates the Levenshtein distance between two string arguments"""

    # Compute Levenshtein distance using helper function and return result
    return _levenshtein_compute(source, target, False)


def levenshtein_norm(source, target):
    """Calculates the normalized Levenshtein distance between two string
    arguments. The result will be a float in the range [0.0, 1.0], with 1.0
    signifying the biggest possible distance between strings with these lengths
    """

    # Compute Levenshtein distance using helper function. The max is always
    # just the length of the longer string, so this is used to normalize result
    # before returning it
    distance = _levenshtein_compute(source, target, False)
    return float(distance) / max(len(source), len(target))
