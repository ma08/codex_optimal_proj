

from operator import itemgetter


def get_max_possible_sum(cards, K):
    cards.sort(key=itemgetter(1), reverse=True)  # 降順
    return sum(card[1] for card in cards[:K])  # 降順に並んだK枚のカードの合計値


A, B, C, K = map(int, input().split())  # 入力
cards = [('A', A), ('B', B), ('C', C)]  # カードのリスト
print(get_max_possible_sum(cards, K))  # 出力
