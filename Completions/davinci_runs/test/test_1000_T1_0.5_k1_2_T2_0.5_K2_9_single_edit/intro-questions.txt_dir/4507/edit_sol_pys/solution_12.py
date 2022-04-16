

from heapq import heappop, heappush

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

shovels = [(a[i], i) for i in range(n)]
heap = []

for _ in range(m):
    heappush(heap, (x, y)) # x is the number of shovels to be bought, y is the discount

shovels.sort(reverse=True)

ans = 0

while k > 0:
    amount, cost = 0, 0
    while amount < k and shovels:
        shovel, shovel_cost = heappop(shovels)
        amount += 1
        cost += shovel_cost
    if not heap:
        ans += cost
        break
    x, y = heappop(heap) # x is the number of shovels to be bought, y is the discount
    if amount <= x:
        ans += cost
        k -= amount
    else:
        ans += cost - y * shovels[-y][0]
        k -= x

print(ans)
