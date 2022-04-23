

n, m = map(int, input().split())

cost = []
for _ in range(n):
  a, b = map(int, input().split())
  cost.append((a, b))

cost.sort()

prices = 0
for c in cost:
  if m - c[1] > 0:
    prices += c[0] * c[1]
    m -= c[1]
  else:
    prices += c[0] * m
    break

print(prices)
