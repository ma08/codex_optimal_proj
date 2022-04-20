import math


# 入力
N, K = map(int, input().split())  # N: 数列の長さ, K: 何番目までの和を求めるか
p = list(map(int, input().split()))  # p: 数列

# 数列を昇順にソート
p.sort()

# output
print(sum(p[:K]))
