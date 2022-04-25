# -*- coding: utf-8 -*-

import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) <= k * d:
        print(abs(x - (x // d) * d))
    else:
        print(abs(x) - (k * d))

if __name__ == '__main__':
    main()
