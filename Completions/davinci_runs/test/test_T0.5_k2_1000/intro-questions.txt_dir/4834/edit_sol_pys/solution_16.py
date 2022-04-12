#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    times = sorted([int(x) for x in sys.stdin.readline().split()])

    a = 0
    b = 0
    for i in range(n):
        if i % 2 == 0:
            a += times[i]
        else:
            b += times[i]

    print(max(a, b))

if __name__ == '__main__':
    main()
