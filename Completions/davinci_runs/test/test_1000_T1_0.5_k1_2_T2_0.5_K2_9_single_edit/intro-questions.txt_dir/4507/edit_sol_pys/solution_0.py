
from heapq import heappop, heappush

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

shovels = [(a[i], i) for i in range(n)]  # (shovel_cost, shovel_amount)
heap = []

for _ in range(m):
    x, y = map(int, input().split())
    heappush(heap, (x, y))  # (x, y)

shovels.sort()

ans = 0

while k > 0:
    shovel_amount, shovel_cost = 0, 0
    while shovel_amount < k and shovels:
        shovel, shovel_cost = heappop(shovels)
        amount += 1
        cost += shovel_cost
    if not heap:
        ans += cost
        break
    x, y = heappop(heap)
    if amount <= x:
        ans += cost
        k -= amount
    else:
        ans += cost - y * shovels[-y][0]
        k -= x

print(ans)
