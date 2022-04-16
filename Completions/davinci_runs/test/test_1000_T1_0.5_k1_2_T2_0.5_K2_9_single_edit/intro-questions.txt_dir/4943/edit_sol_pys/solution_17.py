
from math import sqrt
from sys import stdin
from collections import namedtuple
from decimal import Decimal
from itertools import count, chain
from fractions import Fraction
from operator import mul
from functools import reduce

Point = namedtuple('Point', 'x y')

def area(points):
    return Decimal(abs(sum(x0*y1 - x1*y0
                         for ((x0, y0), (x1, y1)) in zip(points, chain(points[1:], points[0:1]))))) / 2

def centroid(points):
    return Point(sum(x for x, y in points) / len(points),
                 sum(y for x, y in points) / len(points))

def scale_points(points, scaling_factor):
    c = centroid(points)
    return [Point(x*scaling_factor + c.x*(1-scaling_factor), y*scaling_factor + c.y*(1-scaling_factor)) for x, y in points]

def scale_area(points, target_area):
    return scale_points(points, sqrt(target_area / area(points)))

def read_points(input):
    n = int(input.readline())
    return [Point(*map(Decimal, input.readline().split())) for i in range(n)]

def main():
    points = read_points(stdin)
    target_area = int(stdin.readline())
    scaled_points = scale_area(points, target_area)
    print('\n'.join('{0:.6f} {1:.6f}'.format(x, y) for x, y in scaled_points))

if __name__ == '__main__':
    main()
