

import sys


def count_digits(n, k):
    if n % 2 == 0:
        return "YES"
    elif k % 2 == 0:
        return "YES"
    return "NO"


n, k = map(int, sys.stdin.readline().split())
print(count_digits(n, k))
