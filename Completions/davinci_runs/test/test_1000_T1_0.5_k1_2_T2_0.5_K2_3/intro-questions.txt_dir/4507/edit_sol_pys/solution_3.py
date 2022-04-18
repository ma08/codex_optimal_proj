
from heapq import heappop, heappush

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

shovels = [(a[i], i) for i in range(n)]  # (cost, amount)
heap = []

for _ in range(m):
    x, y = map(int, input().split())
    heappush(heap, (x, y))

shovels.sort()

ans = 0

while k > 0:
    amount, cost = 0, 0
    while amount < k and shovels:
        shovel, shovel_amount = heappop(shovels)
        amount += 1
        cost += shovel_amount
    if not heap:
        ans += cost
        break
    x, y = heappop(heap)
    if amount <= x:
        ans += cost
        k -= amount
    else:
        ans += cost - y * shovels[-1][1]
        k -= x

print(ans)
