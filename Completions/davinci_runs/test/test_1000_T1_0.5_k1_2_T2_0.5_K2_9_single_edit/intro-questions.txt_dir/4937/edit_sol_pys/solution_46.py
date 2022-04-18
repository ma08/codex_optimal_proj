#!/usr/bin/env python3

import sys


def main():
    n, a = map(int, sys.stdin.readline().split())
    e = list(map(int, sys.stdin.readline().split()))
    e.sort()
    e.reverse()
    count = 0
    for i in e:
        if a >= i:
            count += 1
            a -= i
    print(count)


if __name__ == '__main__':
    main()
