from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1))
    return sum(card[1] for card in cards[:K])[::-1]

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards))
