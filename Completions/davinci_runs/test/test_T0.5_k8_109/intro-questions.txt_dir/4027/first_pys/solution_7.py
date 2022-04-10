

import sys

def solve(n):
    if n % 2 == 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(solve(n))