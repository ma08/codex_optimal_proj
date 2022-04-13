from itertools import permutations

x, y, z = map(int, input().split())

# 入力をリストに格納
lst = [x, y, z]

# permutationsで入力を全ての組み合わせに変更
perm = permutations(lst)

# 組み合わせの一つ目の要素と二つ目の要素の差分を取り、それが三つ目の要素と同じかどうかを判定する
for p in perm:
    if p[0] - p[1] == p[2]:
        print(p[1])  # p[1]が答え
        break
    else:
        continue
