
import math


def get_largest_subset(n, points):
    """
    :param n: number of points
    :param points: list of points
    :return: largest subset of points with integral power of 2 distance between each pair of points in the subset
    """
    largest_subset = []
    for i in range(n):
        for j in range(n):
            if i != j and math.log(abs(points[i] - points[j]), 2) % 1 == 0:
                largest_subset.append(points[j])
                break
    return largest_subset


def read_input():
    """
    Reads input, parses it.
    :return: n(int), points(list)
    """
    n = int(input())
    points = [int(i) for i in input().split()]
    return n, points


if __name__ == '__main__':
    n, points = read_input()
    largest_subset = get_largest_subset(n, points)
    print(len(largest_subset))
    print(*largest_subset)
