
import math

n, d = map(int, input().split())

points = []
for _ in range(n):
    points.append(list(map(float, input().split())))

def distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(d)]))

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if distance(points[i], points[j]).is_integer():
            count += 1

print(count)
