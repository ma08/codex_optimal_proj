

import sys
import math

def solve(n, a, b):
    if n <= a:
        return n
    # a + b * k < n <= a + b * (k + 1)
    k = math.ceil((n - a) / b) - 1
    return a + k

if __name__ == "__main__":
    n, a, b = map(int, sys.stdin.readline().strip().split())
    print(solve(n, a, b))