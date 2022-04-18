

from heapq import heappush, heappop # 우선순위 큐
import sys # 입출력

N = int(sys.stdin.readline()) # 입력
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    heappush(heap, num)

while len(heap) > 1:
    a = heappop(heap)
    b = heappop(heap)
    heappush(heap, (a + b) / 2)

print(heap[0])
