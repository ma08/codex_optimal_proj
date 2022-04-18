#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    cnt = 0
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] % 3 == 0:
            cnt += 1
            i += 1
        elif i + 1 < n and a[i] % 3 == 1 and a[i + 1] % 3 == 2:
            cnt += 1
            i += 2
        elif i + 1 < n and a[i] % 3 == 2 and a[i + 1] % 3 == 1:
            cnt += 1
            i += 2
        else:
            i += 1
        if b[j] % 3 == 0:
            cnt += 1
            j += 1
        elif j + 1 < m and b[j] % 3 == 1 and b[j + 1] % 3 == 2:
            cnt += 1
            j += 2
        elif j + 1 < m and b[j] % 3 == 2 and b[j + 1] % 3 == 1:
            cnt += 1
            j += 2
        else:
            j += 1
    print(cnt)

if __name__ == '__main__':
    sys.exit(main())
