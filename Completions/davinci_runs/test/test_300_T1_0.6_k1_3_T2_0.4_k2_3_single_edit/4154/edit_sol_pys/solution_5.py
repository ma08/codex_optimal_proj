
import sys

n, m = map(int, input().split())

# trange[i] はi番目のカードが通れる門の最小値
trange = [sys.maxsize] * n

# 門が通れるカード番号の最小値を求める
for i in range(m):
    l, r = map(int, input().split())
    for j in range(l-1, r):
        trange[j] = r

# 通れる門がm以上あるカードがいくつあるかを求める
print(len([i for i in trange if i >= m]))
