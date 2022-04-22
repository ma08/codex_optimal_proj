

N, M = map(int, input().split())

cost = []
for _ in range(N):
  a, b = map(int, input().split())
  cost.append((a, b))

cost.sort()

price = 0
for c in cost:
  if M - c[1] > 0:
    price += c[0] * c[1]
    M -= c[1]
  else:
    price += c[0] * M
    break

print(price)
