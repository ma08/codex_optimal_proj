
import sys

n, x = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

d = 0
cnt = 0

for v in l:
    d += v
    if d <= x:
        cnt += 1

print(cnt + 1)
