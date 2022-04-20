

N, X = [int(x) for x in input().split()]
cities = [int(x) for x in input().split()]

max_dist = 0
for city in cities:
    dist = abs(X - city)
    if dist > max_dist:
        max_dist = dist

print(max_dist)