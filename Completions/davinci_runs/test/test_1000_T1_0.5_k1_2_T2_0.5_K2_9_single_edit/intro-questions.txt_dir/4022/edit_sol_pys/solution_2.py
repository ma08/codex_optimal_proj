

import numpy as np

f = open('file.txt', 'r')
lines = f.readlines()
f.close()

n = int(lines[0])
lines = lines[1:]
lines = np.array(lines)

print(n)
print(lines)

def get_min_intersection(lines):
    segments = []
    for i in range(n):
        l, r = map(int, lines[i].split())
        segments.append((l, r))

    segments.sort()

    heap = [float('-inf')]
    min_intersection = float('inf')

    for l, r in segments:
        min_intersection = min(min_intersection, heap[0] - l)
        heapq.heappush(heap, r)

    return min_intersection

print(get_min_intersection(lines))
