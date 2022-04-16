
from heapq import heappop, heappush

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

shovels = []
for i in range(n):
    heappush(shovels, (a[i], i))
heap_of_transporters = []

for _ in range(m):
    x, y = map(int, input().split())
    heappush(heap_of_transporters, (x, y))
ans = 0

while k > 0:
    amount, cost = 0, 0  # количество и стоимость копанных лопатами ям
    while amount < k and shovels:
        shovel_cost = heappop(shovels)[0]
        amount += 1
        cost += shovel_cost
    if not heap_of_transporters:
        ans += cost
        break
    x, y = heappop(heap_of_transporters)
    if amount <= x:
        ans += cost
        k -= amount
    else:
        ans += cost - y * shovels[0][0]
        k -= x

print(ans)
