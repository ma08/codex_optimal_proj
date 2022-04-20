# coding: utf-8

from operator import itemgetter

def get_max_possible_sum(cards, K):
    cards.sort(key=itemgetter(0), reverse=True)
    return sum(card[0] for card in cards[:K])

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards, K))
