

import sys, heapq

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

heapq.heapify(A)

for _ in range(M):
    max_value = heapq.heappop(A)
    heapq.heappush(A, max_value // 2)

print(sum(A))
