import sys
import math

n = int(sys.stdin.readline())
points = []

for i in range(n):
    x, y = map(float, sys.stdin.readline().split()) # map() applies a function to every element of an iterable
    points.append((x, y))

def get_angle(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)

angles = []
for i in range(n):
    for j in range(i+1, n):
        a = get_angle(points[i][0], points[i][1], points[j][0], points[j][1])
        angles.append(a)

angles.sort()

max_diff = -1
for i in range(len(angles)-1):
    diff = angles[i+1] - angles[i]
    if diff > max_diff:
        max_diff = diff

print(max_diff * 180 / math.pi)
