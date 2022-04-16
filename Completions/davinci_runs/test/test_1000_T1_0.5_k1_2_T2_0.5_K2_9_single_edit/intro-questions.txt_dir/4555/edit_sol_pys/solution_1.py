
import heapq
import sys

# a, b, k = map(int, input().split())

# h = []
# for i in range(a, b+1):
#     heapq.heappush(h, i)

# for i in range(k):
#     print(heapq.heappop(h))

# for i in range(k):
#     print(heapq.heappop(h[::-1]))

a, b, k = map(int, sys.stdin.readline().split())

h = [i for i in range(a, b+1)]

heapq.heapify(h)

for i in range(k-1):
    heapq.heappop(h)

print(heapq.heappop(h))
