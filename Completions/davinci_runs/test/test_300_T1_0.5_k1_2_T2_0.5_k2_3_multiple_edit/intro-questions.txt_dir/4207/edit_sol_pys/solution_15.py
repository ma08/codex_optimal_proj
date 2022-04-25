

import math

def solve(a, b):
    c = [a1 + b1 for a1, b1 in zip(a, b)]
    c.sort()
    zero_index = bisect.bisect_left(c, 0)
    return zero_index + (len(c) - zero_index - 1)


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(solve(a, b))
