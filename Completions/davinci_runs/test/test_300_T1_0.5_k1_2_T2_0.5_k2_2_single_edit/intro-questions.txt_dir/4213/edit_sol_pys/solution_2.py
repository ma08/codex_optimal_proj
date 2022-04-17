

import sys, heapq

N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(lambda x: int(x) * -1, sys.stdin.readline().rstrip().split()))

heapq.heapify(A)
for i in range(K):
    print(heapq.heappop(A) * -1)

