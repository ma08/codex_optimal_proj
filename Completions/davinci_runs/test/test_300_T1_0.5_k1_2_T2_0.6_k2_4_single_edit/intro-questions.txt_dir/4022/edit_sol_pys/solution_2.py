

#!/usr/bin/python3

# The idea is to use a heap to keep track of the right endpoint of the
# previous segment, and then just pop the first element, which will be
# the minimum.

import heapq

n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

segments.sort()

heap = [float('-inf')]
min_intersection = float('inf')

for l, r in segments:
    min_intersection = min(min_intersection, heap[0] - l)
    heapq.heappush(heap, r)

print(min_intersection)
