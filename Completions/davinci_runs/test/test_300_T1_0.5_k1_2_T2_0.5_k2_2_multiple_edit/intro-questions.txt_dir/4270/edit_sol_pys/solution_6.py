#

import sys
import heapq
import math

num = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))
heapq.heapify(v)

for i in range(num-1):
    x = heapq.heappop(v)
    y = heapq.heappop(v)
    heapq.heappush(v, math.floor((x+y)/2))

print(v[0])
