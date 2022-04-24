
n, m = map(int, input().split())

cost = []
for _ in range(n):
    a, b = map(int, input().split())
    cost.append((a, b))

cost.sort()

price = 0
for c in cost:
    if m - c[1] > 0:
        price += c[0] * c[1]
        m -= c[1]
    else:
        price += c[0] * m
        break
print(price)
