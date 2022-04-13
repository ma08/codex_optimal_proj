

from math import sqrt
from sys import stdin

def read_input():
    N = int(stdin.readline().strip())
    points = []
    for i in range(N):
        x, y = [int(x) for x in stdin.readline().strip().split()]
        points.append((x, y))
    A = int(stdin.readline().strip())
    return N, points, A

def print_output(points):
    for x, y in points:
        print("%d %d"%(x, y))

def get_area(points):
    area = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % len(points)]
        area += x1*y2 - x2*y1
    return area / 2

def get_centroid(points):
    x_sum = 0
    y_sum = 0
    for x, y in points:
        x_sum += x
        y_sum += y
    return x_sum / len(points), y_sum / len(points)

def get_rescaled_points(points, A):
    old_area = get_area(points)
    ratio = sqrt(A / old_area)
    cx, cy = get_centroid(points)
    rescaled_points = []
    for x, y in points:
        rescaled_points.append(((x-cx)*ratio, (y-cy)*ratio))
    return rescaled_points

def main():
    N, points, A = read_input()
    rescaled_points = get_rescaled_points(points, A)
    print_output(rescaled_points)

if __name__ == '__main__':
    main()
