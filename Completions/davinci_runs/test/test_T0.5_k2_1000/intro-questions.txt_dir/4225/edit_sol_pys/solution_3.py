from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True) # sort cards by the second element of each tuple
    return sum(card[1] for card in cards[:K]) # return the sum of the first K cards

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards))
