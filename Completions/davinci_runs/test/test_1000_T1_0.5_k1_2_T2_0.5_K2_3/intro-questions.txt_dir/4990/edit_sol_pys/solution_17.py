

import sys, math

def solve():
    b, k, g = map(int, sys.stdin.readline().strip().split())
    if k % g == 0:
        return k // g
    else:
        return math.ceil(k / g)

print(solve())
