#!/usr/bin/env python3
# coding: utf-8

import sys
import math

def main():
    n, m = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    print(solve(n, m, p))

def solve(n, m, p):
    left, right = 1, n
    mid = (left + right) // 2
    count = 0
    while left <= right:
        c = 0
        for i in p:
            if i == mid:
                c += 1
        if c == m:
            count += 1
            for i in range(m):
                for j in range(i + 1, m):
                    count += j - i
                    break
            break
        elif c > m:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    print(count)
    return count

if __name__ == "__main__":
    main()
