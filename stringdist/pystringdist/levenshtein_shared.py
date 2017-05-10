# Copyright (c) 2017 Oleg Bulkin
# MIT License (https://opensource.org/licenses/MIT)


def _levenshtein_compute(source, target, rd_flag):
    """Computes the Levenshtein
    (https://en.wikipedia.org/wiki/Levenshtein_distance)
    and restricted Damerau-Levenshtein
    (https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
    distances between two Unicode strings with given lengths using the
    Wagner-Fischer algorithm
    (https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm).
    These distances are defined recursively, since the distance between two
    strings is just the cost of adjusting the last one or two characters plus
    the distance between the prefixes that exclude these characters (e.g. the
    distance between "tester" and "tested" is 1 + the distance between "teste"
    and "teste"). The Wagner-Fischer algorithm retains this idea but eliminates
    redundant computations by storing the distances between various prefixes in
    a matrix that is filled in iteratively.
    """

    # Create matrix of correct size (this is s_len + 1 * t_len + 1 so that the
    # empty prefixes "" can also be included). The leftmost column represents
    # transforming various source prefixes into an empty string, which can
    # always be done by deleting all characters in the respective prefix, and
    # the top row represents transforming the empty string into various target
    # prefixes, which can always be done by inserting every character in the
    # respective prefix. The ternary used to build the list should ensure that
    # this row and column are now filled correctly
    s_range = range(len(source) + 1)
    t_range = range(len(target) + 1)
    matrix = [[(i if j == 0 else j) for j in t_range] for i in s_range]

    # Iterate through rest of matrix, filling it in with Levenshtein
    # distances for the remaining prefix combinations
    for i in s_range[1:]:
        for j in t_range[1:]:
            # Applies the recursive logic outlined above using the values
            # stored in the matrix so far. The options for the last pair of
            # characters are deletion, insertion, and substitution, which
            # amount to dropping the source character, the target character,
            # or both and then calculating the distance for the resulting
            # prefix combo. If the characters at this point are the same, the
            # situation can be thought of as a free substitution
            del_dist = matrix[i - 1][j] + 1
            ins_dist = matrix[i][j - 1] + 1
            sub_trans_cost = 0 if source[i - 1] == target[j - 1] else 1
            sub_dist = matrix[i - 1][j - 1] + sub_trans_cost

            # Choose option that produces smallest distance
            matrix[i][j] = min(del_dist, ins_dist, sub_dist)

            # If restricted Damerau-Levenshtein was requested via the flag,
            # then there may be a fourth option: transposing the current and
            # previous characters in the source string. This can be thought of
            # as a double substitution and has a similar free case, where the
            # current and preceeding character in both strings is the same
            if rd_flag and i > 1 and j > 1 and source[i - 1] == target[j - 2] \
                    and source[i - 2] == target[j - 1]:
                trans_dist = matrix[i - 2][j - 2] + sub_trans_cost
                matrix[i][j] = min(matrix[i][j], trans_dist)

    # At this point, the matrix is full, and the biggest prefixes are just the
    # strings themselves, so this is the desired distance
    return matrix[len(source)][len(target)]
