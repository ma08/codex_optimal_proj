#!/usr/bin/env python3

import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) <= k * d:
        print(abs(abs(x) - (x // d) * d))
    elif (k - abs(x) // d) % 2 == 0:
        print(abs((k * d) - abs(x)))
    else:
        print(abs(x) - (k * d))

if __name__ == '__main__':
    main()
