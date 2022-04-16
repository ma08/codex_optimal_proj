K = int(input())

from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True) # タプルの2つ目の値で降順にソート
    return sum(card[1] for card in cards[:K]) # タプルの2つ目を取り出して合計

A, B, C, K = map(int, input().split())
cards = [('A', A), ('B', B), ('C', C)]
print(get_max_possible_sum(cards))
