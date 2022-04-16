import math

import sys

def main():
    n = int(sys.stdin.readline())
    print(solve(n))

def solve(n):
    return math.ceil(n/2) - 1

if __name__ == '__main__':
    main()
