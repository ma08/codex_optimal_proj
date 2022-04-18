

import sys
import math

def find_closest_point(x1, y1, x2, y2, x3, y3):
    return 0

def main():
    n = int(sys.stdin.readline())
    points = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        points.append((x,y))
    points = sorted(points, key=lambda x: x[1])
    # print points
    min_dist = 100000
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                dist = find_closest_point(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1])
                if dist < min_dist:
                    min_dist = dist
    print("%.6f" % min_dist)

if __name__ == '__main__':
    main()
