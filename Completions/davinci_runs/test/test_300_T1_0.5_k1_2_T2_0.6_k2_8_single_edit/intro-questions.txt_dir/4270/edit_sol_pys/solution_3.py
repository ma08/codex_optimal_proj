import sys


n = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))

v.sort()

for i in range(num-1):
    x = heapq.heappop(v)
    y = heapq.heappop(v)
    heapq.heappush(v, (x+y)/2)

print(v[0])
