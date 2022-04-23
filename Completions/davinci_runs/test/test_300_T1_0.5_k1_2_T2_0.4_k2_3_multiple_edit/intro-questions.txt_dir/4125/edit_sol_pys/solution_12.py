

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 17:05:54

import sys

def solve(x, xs):
    xs = sorted(xs)
    x_min, x_max = xs[0], xs[-1]
    if x < x_max:
        x_max = x_max + (x_min - x) // 2
    elif x > x_min:
        x_min = x_min - (x - x_max) // 2
    return abs(x_max - x_min)

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(x, xs))

if __name__ == '__main__':
    main()
