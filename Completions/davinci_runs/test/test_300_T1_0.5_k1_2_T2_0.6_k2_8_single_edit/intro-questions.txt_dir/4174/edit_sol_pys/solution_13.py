# https://atcoder.jp/contests/abc081/tasks/abc081_a

import sys

s = list(map(int, sys.stdin.readline().rstrip()))

d = 0
cnt = 0

for i in range(n):
    d += l[i]
    if d <= x:
        cnt += 1

print(cnt + 1)
