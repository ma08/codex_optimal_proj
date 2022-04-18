from itertools import permutations

x, a, b = map(int, input().split()) # 入力を整数に変換

lst = [x, a, b] # 入力をリストに格納する

perm = permutations(lst) # permutationsで入力を全ての組み合わせに変更する

for p in perm:
    if p[0] - p[1] == p[2]: # 組み合わせの一つ目の要素と二つ目の要素の差分を取り、それが三つ目の要素と同じかどうかを判定する
        print(p[1])
        break # 終了
