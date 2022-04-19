
import sys

n, x = map(int, sys.stdin.readline().split())
l = map(int, sys.stdin.readline().split())

d = 0
cnt = 0

for i in l:
    d += i
    if d <= x:
        cnt += 1

print(cnt + 1)
