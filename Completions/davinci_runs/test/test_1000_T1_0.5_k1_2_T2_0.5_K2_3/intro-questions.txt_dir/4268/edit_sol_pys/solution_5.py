import math

n, d = map(int, input().split())

points = []
for _ in range(n):
    points.append(list(map(int, input().split())))

def distance(p1, p2):
    dist = 0
    for i in range(d):
        dist += (p1[i] - p2[i]) ** 2
    return math.sqrt(dist)

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if distance(points[i], points[j]).is_integer(): # is_integer() is used for checking whether the float number is integer or not.
            count += 1

print(count)
