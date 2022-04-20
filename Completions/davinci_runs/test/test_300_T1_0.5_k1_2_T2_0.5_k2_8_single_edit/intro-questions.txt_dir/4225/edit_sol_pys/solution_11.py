
from operator import itemgetter

def get_max_possible_sum(cards, k):
    cards.sort(key=itemgetter(1), reverse=True)  # sort by card value
    return sum(card[1] for card in cards[:k])

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards))
