
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

def print_output(points):
    for x, y in points:
        print(x, y)

def get_area(points):
    area = 0.0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % len(points)]
        area += x1*y2 - x2*y1
    return area / 2.0

def get_centroid(points):
    x_sum = 0.0
    y_sum = 0.0
    for x, y in points:
        x_sum += x
        y_sum += y
    return x_sum / len(points), y_sum / len(points)

def get_resized_points(points, A):
    old_area = get_area(points)
    ratio = sqrt(A / old_area)
    cx, cy = get_centroid(points)
    resized_points = []
    for x, y in points:
        resized_points.append(((x-cx)*ratio, (y-cy)*ratio))
    return resized_points

def main():
    N, points, A = read_input()
    resized_points = get_resized_points(points, A)
    print_output(resized_points)

if __name__ == '__main__':
    main()
