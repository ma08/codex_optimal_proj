import sys

import heapq

a, b, k = map(int, sys.stdin.readline().split())

h = []
for i in range(a, b + 1):
    heapq.heappush(h, i)

for i in range(k):
    sys.stdout.write(str(heapq.heappop(h)) + '\n')

for i in range(k):
    print(heapq.heappop(h[::-1]))
