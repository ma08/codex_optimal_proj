

from math import sqrt
from sys import stdin

def read_input():
    N = int(stdin.readline().strip())
    points = []
    for i in range(N):
        x, y = [float(x) for x in stdin.readline().strip().split()]
        points.append((x, y))
    A = float(stdin.readline().strip())
    return N, points, A

def print_output(rescaled_points):
    for x, y in rescaled_points:
        print("%.2f %.2f" % (x, y))

def get_area(rescaled_points):
    area = 0.0
    for i in range(len(rescaled_points)):
        x1, y1 = rescaled_points[i]
        x2, y2 = rescaled_points[(i+1) % len(rescaled_points)]
        area += x1*y2 - x2*y1
    return area / 2.0

def get_centroid(rescaled_points):
    x_sum = 0.0
    y_sum = 0.0
    for x, y in rescaled_points:
        x_sum += x
        y_sum += y
    return x_sum / len(rescaled_points), y_sum / len(rescaled_points)

def get_rescaled_points(rescaled_points, A):
    old_area = get_area(rescaled_points)
    ratio = sqrt(A / old_area)
    cx, cy = get_centroid(rescaled_points)
    rescaled_points = []
    for x, y in rescaled_points:
        rescaled_points.append(((x-cx)*ratio, (y-cy)*ratio))
    return rescaled_points

def main():
    N, points, A = read_input()
    rescaled_points = get_rescaled_points(points, A)
    print_output(rescaled_points)

if __name__ == '__main__':
    main()
