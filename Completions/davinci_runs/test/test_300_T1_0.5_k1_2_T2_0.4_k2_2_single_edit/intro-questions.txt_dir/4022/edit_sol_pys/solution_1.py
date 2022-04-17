

# SOLUTION
# The problem is to find the segment with the least intersection length.
# If we sort the segments by their left endpoints, we can consider the
# problem as finding the segment with the least intersection length with
# the segment before it.  We can use a heap to keep track of the right
# endpoint of the previous segment and then just pop the first element,
# which will be the minimum.

# COMPLEXITY
# O(n log n) time and O(n) space.

import heapq

n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

segments.sort()

heap = [-float('inf')]
min_intersection = float('inf')

for l, r in segments:
    min_intersection = min(min_intersection, heap[0] - l)
    heapq.heappush(heap, r)

print(min_intersection)
