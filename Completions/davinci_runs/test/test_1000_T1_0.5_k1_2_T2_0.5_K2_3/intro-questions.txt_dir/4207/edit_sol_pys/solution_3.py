import sys
import bisect
import math

def solve(a, b):
    c = [a1+b1 for a1, b1 in zip(a, b)]
    c.sort()
    zero_idx = bisect.bisect_left(c, 0)
    return zero_idx + (len(c) - zero_idx - 1)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    b = [int(x) for x in sys.stdin.readline().split()]
    print(solve(a, b))
