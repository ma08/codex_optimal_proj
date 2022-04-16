
from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True)
    return sum(card[1] for card in cards[:K + 1])

A, B, C, K = map(int, input().split())  # A, B, C: 各カードの枚数、K: 最大で何枚まで選べるか
cards = [('A', A), ('B', B), ('C', C)]  # カード名と枚数のタプルのリスト
print(get_max_possible_sum(cards))
