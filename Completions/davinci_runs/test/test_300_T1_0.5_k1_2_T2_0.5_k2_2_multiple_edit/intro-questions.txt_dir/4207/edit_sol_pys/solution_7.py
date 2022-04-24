

import bisect

def solve(a, b):
    c = [a1+b1 for a1, b1 in zip(a, b)]
    c.sort()
    zero_idx = bisect.bisect_left(c, 0)
    return zero_idx + len(c) - zero_idx - 1


if __name__ == '__main__':
    n = int(input())  # read a line with a single integer
    a = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    b = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    print(solve(a, b))
