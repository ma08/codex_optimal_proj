#!/usr/bin/env python3

from operator import itemgetter


A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards))
