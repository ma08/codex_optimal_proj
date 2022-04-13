from operator import itemgetter

def get_max_possible_sum(cards):
    K = min(K, len(cards))
    cards.sort(key=itemgetter(1), reverse=True)
    return sum(card[1] for card in cards[:K])

A, B, C, K = map(int, input().split()) # 2 1 3 2
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards))
