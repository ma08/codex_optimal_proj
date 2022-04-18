

import sys, heapq

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))[:n]

heapq.heapify(p)

for _ in range(n):
    print(heapq.heappop(p))
