

import heapq

n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

# We can use a heap to keep track of the right endpoint of the previous
# segment and then just pop the first element, which will be the
# smallest.

import heapq

n = int(input())
segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

segments.sort()

heap = [float('-inf')]
smallest_intersection = float('inf')

for l, r in segments:
    smallest_intersection = min(smallest_intersection, heap[0] - l)
    heapq.heappush(heap, r)

print(smallest_intersection)
