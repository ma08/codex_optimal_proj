

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
    a.sort()
    if a[-1] % 2 == 0 and a[-1] != 0:
        a[-1] //= 2
        a.append(a[-1])
        return 1 + solve(n + 1, k, a)
    else:
        if a[-1] != 0:
            a[-2] //= 2
            a[-1] //= 2
            if a[-1] == a[-2]:
                return 1 + solve(n, k, a)
            else:
                a.append(a[-1])
                return 1 + solve(n + 1, k, a)
        else:
            return -1


def main():
    n, k = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print(solve(n, k, a))


if __name__ == '__main__':
    main()
