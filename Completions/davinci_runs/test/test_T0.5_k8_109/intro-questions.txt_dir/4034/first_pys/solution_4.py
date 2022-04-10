

from collections import Counter
from itertools import permutations
from typing import List

from utils.input_parsers import parse_single_line_string


def get_sorted_permutations(s: str) -> List[str]:
    """
    Get all possible permutations of the given string, sorted by length.
    """
    return sorted(set(permutations(s)), key=len)


def get_swaps(s: str, t: str) -> int:
    """
    Get the number of swaps required to transform the string s into the string t.
    """
    swaps = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            swaps += 1
    return swaps


def is_sorted_by_swaps(s: str, t: str) -> bool:
    """
    Check if the given string can be transformed into the given string using swaps.
    """
    return get_swaps(s, t) <= 1


def get_swap_pairs(s: str) -> List[str]:
    """
    Get all possible pairs of characters that can be swapped.
    """
    swap_pairs = []
    for i in range(len(s) - 1):
        swap_pairs.append(s[i:i + 2])
    return swap_pairs


def get_swap_pair_counts(s: str) -> Counter:
    """
    Get a counter of the number of times each pair of characters appears in the given string.
    """
    return Counter(get_swap_pairs(s))


def get_swap_pair_counts_diff(s: str, t: str) -> Counter:
    """
    Get a counter of the difference in the number of times each pair of characters appears in the given strings.
    """
    return get_swap_pair_counts(s) - get_swap_pair_counts(t)


def get_swap_pair_counts_diff_sum(s: str, t: str) -> int:
    """
    Get the sum of the difference in the number of times each pair of characters appears in the given strings.
    """
    return sum(get_swap_pair_counts_diff(s, t).values())


def get_swap_pair_counts_diff_sum_permutations(s: str) -> int:
    """
    Get the sum of the difference in the number of times each pair of characters appears in the given string and each
    permutation of the given string.
    """
    return sum(get_swap_pair_counts_diff_sum(s, t) for t in get_sorted_permutations(s))


def get_sorted_permutations_swap_pair_counts_diff_sum(s: str) -> int:
    """
    Get the sum of the difference in the number of times each pair of characters appears in the given string and each
    permutation of the given string, sorted by length.
    """
    return sum(get_swap_pair_counts_diff_sum(s, t) for t in get_sorted_permutations(s))


def is_sorted_by_swaps_permutations(s: str) -> bool:
    """
    Check if the given string can be transformed into any permutation of the given string using swaps.
    """
    return get_sorted_permutations_swap_pair_counts_diff_sum(s) == 0


def is_sorted_by_swaps_permutations_coloring(s: str) -> bool:
    """
    Check if the given string can be transformed into any permutation of the given string using swaps and coloring.
    """
    return get_sorted_permutations_swap_pair_counts_diff_sum(s) % 2 == 0


def get_sorted_permutations_swap_pair_counts_diff_sum_coloring(s: str) -> int:
    """
    Get the sum of the difference in the number of times each pair of characters appears in the given string and each
    permutation of the given string, sorted by length, if coloring is used.
    """
    return get_sorted_permutations_swap_pair_counts_diff_sum(s) // 2


def get_coloring(s: str) -> str:
    """
    Get a coloring of the given string.
    """
    return ''.join(['0' if get_sorted_permutations_swap_pair_counts_diff_sum_coloring(s) % 2 == 0 else '1'] * len(s))


if __name__ == '__main__':
    n = int(input())
    s = parse_single_line_string(input())

    if is_sorted_by_swaps_permutations_coloring(s):
        print('YES')
        print(get_coloring(s))
    else:
        print('NO')