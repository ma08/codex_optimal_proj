#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def solve(n, a):
    """
    >>> solve(3, [1, 2, 3])
    1
    >>> solve(3, [1, 3, 2])
    2
    >>> solve(3, [2, 1, 3])
    2
    >>> solve(3, [2, 3, 1])
    2
    >>> solve(3, [3, 1, 2])
    2
    >>> solve(3, [3, 2, 1])
    3
    >>> solve(4, [1, 2, 3, 4])
    1
    >>> solve(4, [1, 3, 2, 4])
    2
    >>> solve(4, [1, 4, 2, 3])
    2
    >>> solve(4, [2, 1, 3, 4])
    2
    >>> solve(4, [2, 3, 1, 4])
    2
    >>> solve(4, [2, 4, 1, 3])
    2
    >>> solve(4, [3, 1, 2, 4])
    2
    >>> solve(4, [3, 2, 1, 4])
    2
    >>> solve(4, [3, 4, 1, 2])
    2
    >>> solve(4, [4, 1, 2, 3])
    2
    >>> solve(4, [4, 2, 1, 3])
    2
    >>> solve(4, [4, 3, 1, 2])
    3
    """
    min_count = sys.maxsize
    for v in range(1, n + 1):
        count = 0
        for i, x in enumerate(a):
            if x != v:
                count += 1
                if i + 1 < n and a[i + 1] == v:
                    a[i], a[i + 1] = a[i + 1], a[i]
                else:
                    a[i], a[i - 1] = a[i - 1], a[i]
        min_count = min(count, min_count)
    return min_count


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print(solve(n, a))
