

import sys
import heapq

num = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))
heapq.heapify(v)  # O(N)

for i in range(num-1):  # O(NlogN)
    x = heapq.heappop(v)  # O(logN)
    y = heapq.heappop(v)  # O(logN)
    heapq.heappush(v, (x+y)/2)  # O(logN)

print(v[0])  # O(1)
