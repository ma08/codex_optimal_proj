

from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True)
    return sum(card[1] if card[1] > 0 else 0 for card in cards[:K])

A, B, C, K = map(int, input().split()) # 1 2 3 4
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards))
