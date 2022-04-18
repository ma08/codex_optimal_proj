

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
import heapq

heapq.heapify(a)

for i in range(n-1):
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    heapq.heappush(a, (x+y)/2)

print(a[0])
