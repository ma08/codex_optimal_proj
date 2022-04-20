

def find_subset(n, points):
    points.sort()
    distances = []
    for i in range(n - 1):
        distances.append(points[i+1] - points[i])
    subset = []
    i = 0
    while i < n - 1:
        if distances[i] == 1:
            subset.append(points[i+1])
            i += 1
        elif distances[i] == 2:
            subset.append(points[i+1])
            i += 2
        else:
            i += 1
    return subset

n = int(input())
points = list(map(int, input().split()))
subset = find_subset(n, points)
print(len(subset))
print(*subset)