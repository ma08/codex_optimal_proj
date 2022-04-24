

from heapq import heappush, heappop, heapify
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    heappush(heap, (-num, num))

while len(heap) > 1:
    a = heappop(heap)[1]
    b = heappop(heap)[1]
    heappush(heap, (-(a + b) / 2, (a + b) / 2))

print(heap[0])
