

from itertools import permutations

x, a, b = map(int, input().split())  # 入力をリストに格納

lst = [x, a, b]

perm = permutations(lst)  # permutationsで入力を全ての組み合わせに変更

for p in perm:  # 組み合わせの一つ目の要素と二つ目の要素の差分を取り、それが三つ目の要素と同じかどうかを判定
    if p[0] - p[1] == p[2]:
        print(p[1])
        break
    else:
        continue
