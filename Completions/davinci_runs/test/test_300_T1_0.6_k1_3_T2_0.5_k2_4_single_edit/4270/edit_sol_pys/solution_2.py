
from heapq import heappush, heappop
import sys

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline())
    heappush(heap, num)

while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)
    heappush(heap, (a + b) / 2)


print(heap[0])
