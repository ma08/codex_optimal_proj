
from heapq import heappop, heappush, heapify

n, m, k = map(int, input().split())
a = list(map(int, input().split()))  # shovels cost

shovels = [(a[i], i) for i in range(n)]  # (cost, amount)
heap = []  # (cost, amount)

for _ in range(m):
    x, y = map(int, input().split())
    heappush(heap, (x, y))  # (amount, cost)

heapify(shovels)

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
    amount_, cost_ = heappop(heap)
    if amount <= amount_:
        ans += cost
        k -= amount
    else:
        ans += cost - cost_ * shovels[-cost_][1]
        k -= amount_

print(ans)
