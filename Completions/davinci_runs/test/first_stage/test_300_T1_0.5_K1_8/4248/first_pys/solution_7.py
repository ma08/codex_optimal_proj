
from sys import stdin
from math import pi, atan2
from decimal import Decimal


def get_angle(x1, y1, x2, y2):
    return atan2(y2 - y1, x2 - x1)


def get_angle_diff(angle1, angle2):
    diff = abs(angle1 - angle2)
    if diff > pi:
        diff = 2 * pi - diff
    return diff


def get_min_angle_diff(n, points):
    min_angle_diff = 2 * pi
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                angle1 = get_angle(*points[i], *points[j])
                angle2 = get_angle(*points[j], *points[k])
                angle_diff = get_angle_diff(angle1, angle2)
                if angle_diff < min_angle_diff:
                    min_angle_diff = angle_diff
    return min_angle_diff


def main():
    n = int(stdin.readline())
    points = [None] * n
    for i in range(n):
        points[i] = tuple(map(Decimal, stdin.readline().split()))
    print(get_min_angle_diff(n, points))


if __name__ == "__main__":
    main()