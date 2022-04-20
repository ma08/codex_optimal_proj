

from heapq import heappop, heappush

a, b, c, k = map(int, input().split())

h = []

for _ in range(a):
    heappush(h, 1)

for _ in range(b):
    heappush(h, 0)

for _ in range(c):
    heappush(h, -1)

for _ in range(k):
    v = heappop(h)
    heappush(h, v+1)

print(sum(h))