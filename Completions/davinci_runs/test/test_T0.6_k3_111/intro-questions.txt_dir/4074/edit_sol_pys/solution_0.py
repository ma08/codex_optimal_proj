
# SOLUTION
# https://codeforces.com/problemset/problem/1281/A

import re

def shovel_packages(n, k):
    """
    >>> shovel_packages(8, 7)
    2
    >>> shovel_packages(8, 1)
    8
    >>> shovel_packages(6, 10)
    1
    >>> shovel_packages(999999733, 999999732)
    999999733
    >>> shovel_packages(999999733, 999999733)
    1
    """
    x = n // k
    return n // x if n % x == 0 else n // (x + 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    t = int(input())
    for _ in range(t):
        n, k = map(int, re.findall(r"\d+", input()))
        print(shovel_packages(n, k))
