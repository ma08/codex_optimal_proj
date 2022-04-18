

import sys
import math

def main():
    n = int(sys.stdin.readline())
    points = []
    for i in range(n):
        x, y = map(float, sys.stdin.readline().split())
        points.append((x, y))
    A = float(sys.stdin.readline())
    # Find the point closest to the origin
    closest = 0
    for i in range(1, n):
        if points[i][0] ** 2 + points[i][1] ** 2 < points[closest][0] ** 2 + points[closest][1] ** 2:
            closest = i
    # Find the angle between the x-axis and the line from the origin to the closest point
    p1 = points[closest]
    p2 = points[(closest + 1) % n]
    p3 = points[(closest - 1) % n]
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p3[0] - p1[0], p3[1] - p1[1])
    angle = math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / math.sqrt((v1[0] ** 2 + v1[1] ** 2) * (v2[0] ** 2 + v2[1] ** 2)))
    # Find the area of the triangle formed by the origin, the closest point, and the point to the left of the closest point
    area = 0.5 * p1[0] * p2[1] + 0.5 * p2[0] * p3[1] + 0.5 * p3[0] * p1[1]
    # Find the area of the polygon
    area += 0.5 * sum(p1[0] * p2[1] - p1[1] * p2[0] for p1, p2 in zip(points, points[1:] + [points[0]]))
    # Find the new area of the polygon and the new angle of the line from the origin to the closest point
    new_area = A - area
    # Find the new length of the edge from the origin to the closest point
    new_length = math.sqrt(2 * new_area / math.sin(angle))
    # Find the new coordinates of the closest point
    new_p1 = (new_length * math.cos(angle / 2), new_length * math.sin(angle / 2))
    # Find the new coordinates of the other points
    new_points = []
    for i in range(n):
        p1 = new_p1
        p2 = new_points[-1] if len(new_points) else new_p1
        p3 = points[(closest + i) % n]
        v1 = (p2[0] - p1[0], p2[1] - p1[1])
        v2 = (p3[0] - p1[0], p3[1] - p1[1])
        angle = math.acos((v1[0] * v2[0] + v1[1] * v2[1]) / math.sqrt((v1[0] ** 2 + v1[1] ** 2) * (v2[0] ** 2 + v2[1] ** 2)))
        length = math.sqrt(2 * new_area / math.sin(angle))
        new_points.append((length * math.cos(angle / 2), length * math.sin(angle / 2)))
    # Output
    for x, y in new_points:
        print("%.4f %.4f" % (x, y))

if __name__ == '__main__':
    main()
