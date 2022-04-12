

from math import sqrt
from sys import stdin

def read_input():
    N = int(stdin.readline().strip())
    points = []
    for i in range(N):
        x, y = [float(x) for x in stdin.readline().strip().split()]
        points.append((x, y))
    area = float(stdin.readline().strip())
    return N, points, area

def print_output(points):
    for x, y in points:
        print(x, y)

def get_area(points):
    area = 0.0
    for i in range(len(points)-1):
        x1, y1 = points[i] 
        x2, y2 = points[i+1]
        area += x1*y2 - x2*y1
    x1, y1 = points[len(points)-1]
    x2, y2 = points[0]
    area += x1*y2 - x2*y1
    area = abs(area)
    return area / 2.0

def get_centroid(points):
    x_sum = 0.0
    y_sum = 0.0
    for x, y in points:
        x_sum += x
        y_sum += y
    return x_sum / len(points), y_sum / len(points)

def get_resized_points(points, area):
    old_area = get_area(points)
    ratio = sqrt(area / old_area)
    cx, cy = get_centroid(points)
    resized_points = []
    for x, y in points:
        resized_points.append(((x-cx)*ratio, (y-cy)*ratio))
    return resized_points

def main():
    N, points, area = read_input()
    resized_points = get_resized_points(points, area)
    print_output(resized_points)

if __name__ == '__main__':
    main()
