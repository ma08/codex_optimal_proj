

from operator import itemgetter

def get_max_possible_sum(cards, K):
    cards.sort(key=itemgetter(1), reverse=True) # sort by second item
    return sum(card[1] for card in cards[:K]) # sum of first K items

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards, K))
