import sys, heapq

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
heapq.heapify(arr)

for _ in range(M):
    tmp = heapq.heappop(arr)
    heapq.heappush(arr, tmp // 2)

print(sum(arr))
