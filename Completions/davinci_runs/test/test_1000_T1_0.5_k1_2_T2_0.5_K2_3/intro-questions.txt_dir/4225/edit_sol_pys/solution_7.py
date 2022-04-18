
from operator import itemgetter

def get_max_possible_sum(cards, K):
    cards.sort(key=itemgetter(1))
    return sum(card[1] for card in cards[:K]) if K <= len(cards) else sum(card[1] for card in cards)

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards, K))
