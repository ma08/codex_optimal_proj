
import heapq
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
prices = list(map(int, sys.stdin.readline().rstrip().split()))
heapq.heapify(prices)

total = 0
for i in range(K):
    total += heapq.heappop(prices)

print(total)
