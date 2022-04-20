# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-09-30 10:48:04
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-09-30 10:48:04

import sys

def solve():
    h, n = map(int, input().split())
    d = list(map(int, input().split()))
    for i in range(n):
        h += d[i]
        if h <= 0:
            return i + 1
    return -1

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    print(solve())
