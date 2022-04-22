
from sys import stdin

n, x = list(map(int, stdin.readline().split()))
l = list(map(int, stdin.readline().split()))
d = 0
cnt = 0

for i in range(n):
    d += l[i]
    if d <= x:
        cnt += 1

print(cnt + 1)
