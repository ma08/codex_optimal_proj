import sys

n, x = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split())

d, cnt = 0, 1

for i in range(n):
    if d + l[i] <= x:
        d += l[i]
        cnt += 1

print(cnt)
