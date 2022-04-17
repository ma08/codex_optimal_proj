

from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True)
    return sum(card[1] for card in cards[:K] if card[1] > 0)

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C), ('D', D)]
print(get_max_possible_sum(cards))
