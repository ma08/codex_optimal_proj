

n, m = map(int, input().split())

# ε₯ε
roads = []
for i in range(m):
    a, b = map(int, input().split())
    roads.append([a, b])

# εΊε
for i in range(1, n+1):
    count = 0
    for road in roads:
        if i in road:
            count += 1
    print(count)