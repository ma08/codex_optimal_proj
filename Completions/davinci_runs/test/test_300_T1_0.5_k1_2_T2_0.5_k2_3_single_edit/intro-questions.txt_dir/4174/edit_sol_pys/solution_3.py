
import sys

n, x = list(map(int, sys.stdin.readline().split()))
L = list(map(int, sys.stdin.readline().split()))

d = 0  # distance
cnt = 0

for i in range(n):
    d += L[i]
    if d <= x:
        cnt += 1

print(cnt + 1)
