

# SOLUTION 1
# The problem is to find the interval with the least intersection length.
# If we sort the intervals by their left endpoints, we can consider the
# problem as finding the interval with the least intersection length with
# the interval before it.

# To do this, we can keep track of the right endpoint of the previous interval.
# For the first interval, we just set the right endpoint to -infinity.  For the
# next interval, we compute the intersection length and update the right
# endpoint to the right endpoint of the current interval.  We can then keep
# track of the minimum intersection length and return at the end.

# We can use a heap to keep track of the right endpoint of the previous interval
# and then just pop the first element, which will be the minimum.

import heapq

n = int(input())
intervals = []
for i in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

intervals.sort()

heap = [float('-inf')]
min_intersection = float('inf')

for l, r in intervals:
    min_intersection = min(min_intersection, heap[0] - l)
    heapq.heappush(heap, r)

print(min_intersection)

# SOLUTION 2
# The problem is to find the interval with the least intersection length.
# If we sort the intervals by their left endpoints, we can consider the
# problem as finding the interval with the least intersection length with
# the interval before it.

# To do this, we can keep track of the right endpoint of the previous interval.
# For the first interval, we just set the right endpoint to -infinity.  For the
# next interval, we compute the intersection length and update the right
# endpoint to the right endpoint of the current interval.  We can then keep
# track of the minimum intersection length and return at the end.

# We can use a heap to keep track of the right endpoint of the previous interval
# and then just pop the first element, which will be the minimum.

import heapq

n = int(input())
intervals = []
for i in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r))

intervals.sort()

heap = [float('-inf')]
min_intersection = float('inf')

for l, r in intervals:
    min_intersection = min(min_intersection, heap[0] - l)
    heapq.heappush(heap, r)

print(min_intersection)
