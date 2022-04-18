

import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

n = int(input())

segments.sort()

heap = [float('-inf')]
min_intersection = float('inf')

for l, r in segments:
    min_intersection = min(min_intersection, heap[0] - l)
    heapq.heappush(heap, r)

print(min_intersection)
