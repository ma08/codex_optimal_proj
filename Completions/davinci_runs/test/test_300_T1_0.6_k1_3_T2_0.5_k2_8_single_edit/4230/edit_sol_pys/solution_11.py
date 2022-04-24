#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split()))

    p.sort()

    left = p[0] - X
    right = p[-1] - X

    if abs(left) > abs(right):
        if X - left > 0:
            print(X - left)
        else:
            print(abs(left))
    else:
        if X + right > 0:
            print(abs(right))
        else:
            print(X + right)

if __name__ == '__main__':
    main()
