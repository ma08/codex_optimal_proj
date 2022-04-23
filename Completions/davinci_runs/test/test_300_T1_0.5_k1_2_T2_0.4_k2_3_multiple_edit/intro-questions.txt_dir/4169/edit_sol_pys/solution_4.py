import heapq


n, m = map(int, input().split()) # n: number of items, m: number of people

cost = [] # (price, number of people)
for _ in range(n):
  a, b = map(int, input().split())
  cost.append((-a, b))

heapq.heapify(cost)

price = 0
for c in cost:
  if m - c[1] > 0: # if there are more people than the number of items
    price += -c[0] * c[1]
    m -= c[1]
  else:
    price += -c[0] * m
    break

print(price)
