# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    print(solve(n))

def solve(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n // 2 - 1

if __name__ == '__main__':
    main()
