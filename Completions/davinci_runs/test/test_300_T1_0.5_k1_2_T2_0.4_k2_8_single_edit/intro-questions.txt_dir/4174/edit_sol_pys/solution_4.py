

import sys, heapq

n, k = map(int, sys.stdin.readline().split())

h = []
for i in range(n):
    heapq.heappush(h, int(sys.stdin.readline()))

for i in range(n):
    d += l[i]
    if d <= x:
        cnt += 1

print(cnt + 1)
