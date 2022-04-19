
import sys
import heapq

num = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))
heapq.heapify(v) # heapify(iterable) -> None. Transform list x into a heap, in-place, in linear time.

for i in range(num-1):
    x = heapq.heappop(v)
    y = heapq.heappop(v)
    heapq.heappush(v, (x+y)/2) # heappush(heap, item) -> None. Push item onto heap, maintaining the heap invariant.

print(v[0])
