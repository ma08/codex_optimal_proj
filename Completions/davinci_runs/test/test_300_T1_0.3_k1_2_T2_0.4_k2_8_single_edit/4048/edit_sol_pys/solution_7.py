

import sys, heapq

N, K = map(int, sys.stdin.readline().split())

heap = []
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

for _ in range(K):
    print(heapq.heappop(heap))
