

from heapq import heappop, heappush

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

shovels = [(a[i], i) for i in range(n)]  # (cost, amount)
heap = []

for _ in range(m):
    x, y = map(int, input().split())
    heappush(heap, (x, y))  # (amount, cost)

shovels.sort()

ans = 0

while k > 0:
    amount, cost = 0, 0  # amount of shovels, cost of shovels
    while amount < k and shovels:
        shovel, shovel_cost = heappop(shovels)
        amount += 1
        cost += shovel_cost
    if not heap:
        ans += cost
        break
    x, y = heappop(heap)
    if amount <= x:  # if amount of shovels is less than amount of sand
        ans += cost
        k -= amount
    else:
        ans += cost - y * shovels[-y][0]
        k -= x

print(ans)
