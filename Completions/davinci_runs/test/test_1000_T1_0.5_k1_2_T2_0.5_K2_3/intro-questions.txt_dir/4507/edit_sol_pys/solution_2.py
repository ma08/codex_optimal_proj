

from heapq import heappop, heappush

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

shoes = [(a[i], i) for i in range(n)]
heap = []

for _ in range(m):
    x, y = map(int, input().split())
    heappush(heap, (x, y))

shoes.sort()

ans = 0

while k > 0:
    amount, cost = 0, 0
    while amount < k and shoes:
        shoe, shoe_cost = heappop(shoes)
        amount += 1
        cost += shoe_cost
    if not heap:
        ans += cost
        break
    x, y = heappop(heap)
    if amount <= x:
        ans += cost
        k -= amount
    else:
        ans += cost - y * shoes[-y][1]
        k -= x

print(ans)
