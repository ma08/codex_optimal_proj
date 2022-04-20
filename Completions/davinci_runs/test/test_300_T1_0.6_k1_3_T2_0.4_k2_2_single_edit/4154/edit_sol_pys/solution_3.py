
import sys

N, M = map(int, input().split())

# T[i] はi番目のカードが通れる門の最大値
T = [0] * N

# 門が通れるカード番号を求める
for i in range(m):
    L, R = map(int, input().split())
    for j in range(L-1, R):
        T[j] = R

# 通れる門がm以上あるカードがいくつあるかを求める
print(len([i for i in T if i >= M]))
