
import heapq
import sys

n, m = map(int, sys.stdin.readline().split())

stores = []
for i in range(n):
    stores.append(list(map(int, sys.stdin.readline().split())))

# stores = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# stores.sort(key=lambda x: x[0])

heapq.heapify(stores)

cost = 0
    store = heapq.heappop(stores)
    if m <= store[1]:
        cost += store[0] * m
        break
    else:
        cost += store[0] * store[1]
        m -= store[1]

print(cost)
