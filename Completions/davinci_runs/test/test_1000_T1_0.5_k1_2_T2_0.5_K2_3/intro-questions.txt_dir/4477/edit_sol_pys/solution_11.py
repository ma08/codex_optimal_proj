#!/usr/bin/env python3

import sys

def solve(n):
    count = 0
    for i in range(1, n+1):
        count += i * (9 - n//(10**i)%10)
    return count

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n = int(sys.stdin.readline())
        print(solve(n))

if __name__ == "__main__":
    main()
