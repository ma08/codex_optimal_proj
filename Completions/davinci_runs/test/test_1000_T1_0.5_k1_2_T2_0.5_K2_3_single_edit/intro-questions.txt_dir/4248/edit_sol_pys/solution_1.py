
import sys
import math

n = int(sys.stdin.readline())
points = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

def get_angle(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)

angles = []
for i in range(n):
    for j in range(i+1, n):
        a = get_angle(points[i][0], points[i][1], points[j][0], points[j][1]) % (2 * math.pi)
        angles.append(a)

angles.sort()

max_diff = -1
for i in range(len(angles)):
    diff = angles[(i+1)%len(angles)] - angles[i]
    max_diff = max(max_diff, diff)

print(max_diff * 180 / math.pi)
