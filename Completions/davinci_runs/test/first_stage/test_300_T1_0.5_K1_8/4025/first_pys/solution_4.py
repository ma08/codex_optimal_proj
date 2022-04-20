

import sys

def solve(a, b, c):
    n = a + b + c
    a /= n
    b /= n
    c /= n
    return max(a + (b + c) * 2, b + (a + c) * 2, c + (a + b) * 2)

if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().split())
    print(solve(a, b, c))