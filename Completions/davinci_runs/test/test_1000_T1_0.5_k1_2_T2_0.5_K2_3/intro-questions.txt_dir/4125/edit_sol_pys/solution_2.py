

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:55:40

import sys

def solve(n, x, xs):
    if n == 1:
        return abs(xs[0] - x)
    xs = sorted(xs) + [x]
    xs = sorted(xs)
    if xs.index(x) == 0:
        return xs[1] - x
    elif xs.index(x) == n:
        return x - xs[-2]
    else:
        return min(x - xs[xs.index(x)-1], xs[xs.index(x)+1] - x)

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(n, x, xs))

if __name__ == '__main__':
    main()
