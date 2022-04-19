

# SOLUTION
# The problem is to find the segment with the least intersection length.
# If we sort the segments by their left endpoints, we can consider the
# problem as finding the segment with the least intersection length with
# the segment before it.

# To do this, we can keep track of the right endpoint of the previous
# segment.  For the first segment, we just set the right endpoint to
# -infinity.  For the next segment, we compute the intersection length
# and update the right endpoint to the right endpoint of the current
# segment.  We can then keep track of the minimum intersection length
# and return at the end.

# We can use a heap to keep track of the right endpoint of the previous
# segment and then just pop the first element, which will be the
# minimum.

import heapq

n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split()) # returns a list of integers
    segments.append((l, r)) # appends a list of tuples to the end of the list

segments.sort() # sorts the list of tuples by the first element of the tuple

heap = [float('-inf')] # creates a heap with the value of -infinity
min_intersection = float('inf') # creates a minimum intersection

for l, r in segments: # iterates through each tuple in the list of tuples
    min_intersection = min(min_intersection, heap[0] - l) # updates the minimum intersection
    heapq.heappush(heap, r) # pushes the right value of the tuple to the heap

print(min_intersection)
