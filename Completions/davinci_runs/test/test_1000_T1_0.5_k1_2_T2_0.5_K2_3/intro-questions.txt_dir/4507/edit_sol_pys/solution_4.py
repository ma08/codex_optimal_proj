
from heapq import heappop, heappush, heapify

n, m, k = map(int, input().split())
a = list(map(int, input().split())) # shovels

shovels = [(a[i], i) for i in range(n)] # (amount, cost)
heap = []

for _ in range(m):
    x, y = map(int, input().split())
    heappush(heap, (-y, -x))

heapify(shovels)

ans = 0

while k > 0:
    cost, amount = 0, 0
    while amount < k and shovels: # add shovels
        shovel_amount, shovel_cost = heappop(shovels)
        amount += shovel_amount
        cost += shovel_cost

    if not heap:
        ans += cost
        break
    x, y = heappop(heap)
    if amount <= x:
        ans += cost
        k -= amount
    else:
        ans += cost - y * shovels[-y][1]
        k -= x

print(ans)
