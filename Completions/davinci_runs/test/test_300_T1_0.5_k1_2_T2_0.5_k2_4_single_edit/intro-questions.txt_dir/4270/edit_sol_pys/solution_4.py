
import sys
import heapq

num = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))

for i in range(num-1):
    heapq.heappush(v, (heapq.heappop(v)+heapq.heappop(v))/2)

print(v[0])
