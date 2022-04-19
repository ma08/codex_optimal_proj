#!/usr/bin/env python3

import sys

def main():
    n, m, q = map(int, input().split())
    a = [0] * (m + 1)
    for _ in range(q):
        ai, bi, ci, di = map(int, input().split())
        a[ai] += di
        a[bi] -= di
    for i in range(1, m + 1):
        a[i] += a[i - 1]
    print(max(a))

if __name__ == '__main__':
    main()
