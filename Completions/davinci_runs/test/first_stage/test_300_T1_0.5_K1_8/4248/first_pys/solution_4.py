

import math

def get_angle(x1, y1, x2, y2):
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def get_min_angle(points):
    min_angle = 0
    for i in range(len(points)):
        a1 = get_angle(points[i][0], points[i][1], points[i - 1][0], points[i - 1][1])
        a2 = get_angle(points[i][0], points[i][1], points[i + 1][0], points[i + 1][1])
        angle = abs(a1 - a2)
        if angle < min_angle or i == 0:
            min_angle = angle
    return min_angle

n = int(input())
points = []
for _ in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

points.append(points[0])
points.append(points[1])

print(get_min_angle(points))