

import sys, heapq

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    heapq.heappush(arr, int(sys.stdin.readline()))

for _ in range(M):
    arr[0] = arr[0] // 2
    heapq.heapify(arr)

print(sum(arr))
