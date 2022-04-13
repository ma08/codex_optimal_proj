#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    print(solve(n))

def solve(n):
    return n // 2 - 1 if n % 2 == 0 else n // 2

if __name__ == "__main__":
    main()
