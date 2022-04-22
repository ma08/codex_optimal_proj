

import math

def solve(a, b):
    c = [0] * (len(a) + len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]
    # c = [a1+b1 for a1, b1 in zip(a, b)]
    c.sort()
    zero_idx = bisect.bisect_left(c, 0)
    return zero_idx + (len(c) - zero_idx - 1)


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(solve(a, b))
