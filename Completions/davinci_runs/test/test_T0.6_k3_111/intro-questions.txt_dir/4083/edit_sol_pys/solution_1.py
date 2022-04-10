

from sys import stdin
from collections import defaultdict


def solve(n, k, a):
    """
    :param n: number of elements in a
    :param k: number of equal numbers required
    :param a: array a
    :return: minimum possible number of operations required to obtain at least k equal numbers in the array.
    """
    d = defaultdict(int)
    for num in a:
        d[num] += 1
    if k in d:
        return 0
    return 0


def main():
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print(solve(n, k, a))


if __name__ == '__main__':
    main()
