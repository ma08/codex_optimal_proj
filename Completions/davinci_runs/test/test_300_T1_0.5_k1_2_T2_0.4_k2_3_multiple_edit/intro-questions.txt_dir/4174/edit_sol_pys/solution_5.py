

import sys

n, m = map(int, sys.stdin.readline().split())

l = list(map(int, sys.stdin.readline().split()))

x = 0
cnt = 0

for i in range(n):
    x += l[i]
    if x <= m:
        cnt += 1

print(cnt + 1)
