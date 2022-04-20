
from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True)
    return sum(card[1] for card in cards[:k])

a, b, c, k = map(int, input().split())
cards = [('A', a), ('B', b), ('C', c)]
print(get_max_possible_sum(cards))
