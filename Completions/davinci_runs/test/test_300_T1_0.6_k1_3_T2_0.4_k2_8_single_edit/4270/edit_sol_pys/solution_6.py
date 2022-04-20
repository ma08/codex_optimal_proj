from heapq import heappush, heappop
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    heappush(heap, num)

while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)
    heappush(heap, int((a + b) / 2))

print(heap[0])
