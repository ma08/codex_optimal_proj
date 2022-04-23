
import math

n = int(input())
points = []
for _ in range(n):
    x, y, h = map(int, input().split())
    points.append((x, y, h))

# C_X, C_Y is on the line that connects points with altitude 10^9
# C_X, C_Y is on the line that connects points with altitude 10^9-1
# C_X, C_Y is on the line that connects points with altitude 10^9-2
# ...
# C_X, C_Y is on the line that connects points with altitude 1
# C_X, C_Y is on the line that connects points with altitude 0

for cx in range(0, 101):
    for cy in range(0, 101):
        h = math.inf
        for i in range(n):
            h = min(h, points[i][2] + abs(points[i][0] - cx) + abs(points[i][1] - cy))
        print(cx, cy, h)
