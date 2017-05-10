# Copyright (c) 2017 Oleg Bulkin
# MIT License (https://opensource.org/licenses/MIT)

# Import shared helper
from .levenshtein_shared import _levenshtein_compute


def rdlevenshtein(source, target):
    """Calculates the restricted Damerau-Levenshtein distance (a.k.a. the
    optimal string alignment distance) between two string arguments
    """

    # Compute restricted Damerau-Levenshtein distance using helper function and
    # return result
    return _levenshtein_compute(source, target, True)


def rdlevenshtein_norm(source, target):
    """Calculates the normalized restricted Damerau-Levenshtein distance
    (a.k.a. the normalized optimal string alignment distance) between two
    string arguments. The result will be a float in the range [0.0, 1.0], with
    1.0 signifying the maximum distance between strings with these lengths
    """

    # Compute restricted Damerau-Levenshtein distance using helper function.
    # The max is always just the length of the longer string, so this is used
    # to normalize result before returning it
    distance = _levenshtein_compute(source, target, True)
    return float(distance) / max(len(source), len(target))
