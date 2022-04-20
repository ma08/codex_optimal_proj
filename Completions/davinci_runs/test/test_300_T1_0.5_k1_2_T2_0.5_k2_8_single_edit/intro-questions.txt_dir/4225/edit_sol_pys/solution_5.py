# -*- coding: utf-8 -*-
# @Author: krocki
# @Date:   2017-01-28 19:53:49
# @Last Modified by:   krocki
# @Last Modified time: 2017-01-28 19:54:05

from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True)
    return sum(card[1] for card in cards[:K])

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards))
