
from itertools import combinations

x, a, b = map(int, input().split())

# 入力をリストに格納
lst = [x, a, b]

# combinationsで入力を全ての組み合わせに変更
comb = combinations(lst)

# 組み合わせの一つ目の要素と二つ目の要素の差分を取り、それが三つ目の要素と同じかどうかを判定
for p in comb:
    if p[0] - p[1] == p[2]:
        print(p[1])
        break
    else:
        continue
