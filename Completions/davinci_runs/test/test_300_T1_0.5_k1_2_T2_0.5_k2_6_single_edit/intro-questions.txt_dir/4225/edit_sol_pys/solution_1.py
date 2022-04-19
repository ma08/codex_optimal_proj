#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter

    """
    >>> get_max_possible_sum([('A', 1), ('B', 2), ('C', 3)])
    3
    >>> get_max_possible_sum([('A', 1), ('B', 2), ('C', 3)], 2)
    3
    >>> get_max_possible_sum([('A', 1), ('B', 2), ('C', 3)], 1)
    2
    >>> get_max_possible_sum([('A', 1), ('B', 2), ('C', 3)], 3)
    6
    """
def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True)
    return sum(card[1] for card in cards[:k])


if __name__ == "__main__":
    A, B, C, K = map(int, input().split())
    cards = [('A', A), ('B', B), ('C', C)]
    print(get_max_possible_sum(cards, K))
