#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)

    if a[-1] >= m:
        print(1)
        return

    days = 1
    for i in range(n):
        m -= a[i]
        days += 1
        if m <= 0:
            print(days)
            return

    if m % a[-1] == 0:
        print(days + math.ceil(m / float(a[-1])))
    else:
        print(-1)


if __name__ == "__main__":
    main()
