#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Shlomi Fish <shlomif@cpan.org>
#
# Distributed under terms of the MIT license.
"""

"""

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    a.reverse()
    if a[0] > m:
        print(-1)
        return
    if a[0] == m:
        print(1)
        return
    for i in range(1, n):
        a[i] = max(0, a[i] - i)
    a.sort()
    a.reverse()
    if a[0] == 0:
        print(-1)
        return
    if a[0] == m:
        print(1)
        return
    ans = 0
    while m > 0:
        ans += 1
        m -= a[0]
    print(ans)

if __name__ == '__main__':
    main()
