

def is_power_of_two(n):
    """
    :param n: integer
    :return: True if n is power of 2, False otherwise
    """
    return (n & (n - 1) == 0) and n != 0


def get_largest_subset(n, points):
    """
    :param n: number of points
    :param points: list of points
    :return: largest subset of points with integral power of 2 distance between each pair of points in the subset
    """
    largest_subset = [points[0]]
    for i in range(1, n):
        for j in range(i):
            if is_power_of_two(abs(points[i] - points[j])):
                largest_subset.append(points[i])
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
