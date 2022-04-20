import sys
from heapq import heappush, heappop, heapify



num = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))
heapify(v)

for i in range(num-1):
    x = heappop(v)
    y = heappop(v)
    heappush(v, (x+y)/2)

print(v[0])
