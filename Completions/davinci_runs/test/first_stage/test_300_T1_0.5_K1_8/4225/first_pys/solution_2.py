

from operator import itemgetter

a, b, c, k = map(int, input().split())

# 各カードのペアを作成する
# それぞれのペアの要素は、[数値, 枚数]
cards = [[a, 1], [b, 0], [c, -1]]

# 数値の大きい順にソートする
# それぞれのペアの要素は、[数値, 枚数]
cards = sorted(cards, reverse=True, key=itemgetter(0))

# 数値が大きいものから、K枚を選ぶ
# K枚に達したら、選ぶカードの数値を足し合わせる
# K枚に達したら、ループを抜ける
for i in range(k):
    if i >= cards[i][0]:
        break
    k -= cards[i][0]

print(sum(map(itemgetter(1), cards[:i])))