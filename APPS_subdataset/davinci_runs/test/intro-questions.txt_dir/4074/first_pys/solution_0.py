

# SOLUTION
# https://codeforces.com/problemset/problem/1281/A

import re

def shovelPackages(n, k):
    """
    >>> shovelPackages(8, 7)
    2
    >>> shovelPackages(8, 1)
    8
    >>> shovelPackages(6, 10)
    1
    >>> shovelPackages(999999733, 999999732)
    999999733
    >>> shovelPackages(999999733, 999999733)
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
        print(shovelPackages(n, k))