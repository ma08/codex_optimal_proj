# https://atcoder.jp/contests/abc084/tasks/abc084_c

from operator import itemgetter

def get_max_possible_sum(cards):
    cards.sort(key=itemgetter(1), reverse=True)
    return sum(card[1] for card in cards[:K]) # K番目までのカードのスコアの合計

N = int(input())
cards = []
for _ in range(N):
    C, S, F = map(int, input().split())
    cards.append((C, S, F))

print(get_max_possible_sum(cards))
