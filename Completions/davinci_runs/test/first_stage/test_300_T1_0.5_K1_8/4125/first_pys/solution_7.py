

n, x = map(int, input().split())
cities = list(map(int, input().split()))
cities.sort()

if cities[0] < x:
    max_dist = x - cities[0]
else:
    max_dist = cities[0] - x

for i in range(1, n):
    dist = cities[i] - cities[i-1]
    if dist > max_dist:
        max_dist = dist

print(max_dist)