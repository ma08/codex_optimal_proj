

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:52:31

import sys

def solve(x, xs):
    xs.sort()
    xmin = xs[0]
    xmax = xs[-1]
    if x < xmin:
        xmax = xmax + (xmin - x)
    elif x > xmax:
        xmin = xmin - (x - xmax)
    return xmax - xmin

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(x, xs))

if __name__ == '__main__':
    main()
