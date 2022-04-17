

# The idea is to keep track of the right endpoint of the previous
# segment.  We can use a heap to keep track of the right endpoint of
# the previous segment and then just pop the first element, which will
# be the minimum.

import heapq

n = int(input())
heap = [float('-inf')]
min_intersection = float('inf')

for i in range(n):
    l, r = map(int, input().split())
    min_intersection = min(min_intersection, heap[0] - l)
    heapq.heappush(heap, r)

print(min_intersection)
