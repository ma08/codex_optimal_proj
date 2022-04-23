

from math import sqrt
from sys import stdin, stdout

def solve(a, b):
    m = min(a, b)
    n = max(a, b)
    if n % m == 0:
        return n + (n / m) + (n / m)
    else:
        s = int(sqrt(m))
        while s > 0:
            if m % s == 0:
                return n + (m / s) + (n * s)
            s -= 1
        return n + 2 * m

a, b = map(int, stdin.readline().strip().split())
print(solve(a, b))
