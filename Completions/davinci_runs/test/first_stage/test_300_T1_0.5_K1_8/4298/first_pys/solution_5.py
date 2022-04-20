

import sys


def get_input():
    """
    Gets input from command line.
    :return: number of trees and the distance an inspector can cover.
    """
    n, d = [int(x) for x in sys.stdin.readline().split()]
    return n, d


def get_min_inspectors(n, d):
    """
    Calculates the minimum number of inspectors needed to cover all trees.
    :param n: number of trees
    :param d: the distance an inspector can cover.
    :return: number of inspectors
    """
    if n <= 2 * d:
        return 1
    elif n % (2 * d + 1) == 0:
        return int(n / (2 * d + 1))
    else:
        return int(n / (2 * d + 1)) + 1


if __name__ == '__main__':
    n, d = get_input()
    print(get_min_inspectors(n, d))