#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    a_idx = 0
    b_idx = 0

    while a_idx < n and b_idx < m:
        if a[a_idx] <= b[b_idx]:
            a_idx += 1
        else:
            b_idx += 1

    print(n - a_idx)

if __name__ == '__main__':
    main()
