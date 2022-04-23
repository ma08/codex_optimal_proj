import math

import sys

def get_input():
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        d = list(map(int, sys.stdin.readline().split()))
        d.sort()
        yield n, d

    d = list(map(int, d))
    d.sort()
def solve(n, d):
    if n == 1:
        return d[0] * 2
    if d[0] * d[-1] % d[-2] != 0 or d[0] * d[-1] / d[-2] < d[0]:
        return d[0] * d[-1]
    else:
        return -1

if __name__ == '__main__':
    for n, d in get_input():
        print(solve(n, d))


# test
for n, d in get_input():
    print(solve(n, d))
