

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:52:00

import sys

def solve(x, ys):
    ys = sorted(ys)
    x_min = ys[0]
    x_max = ys[-1]
    if x < x_min:
        x_max += (x_min - x)
    elif x > x_max:
        x_min -= (x - x_max)
    return x_max - x_min

def main():
    n, x = map(int, sys.stdin.readline().split())
    ys = list(map(int, sys.stdin.readline().split()))
    print(solve(x, ys))

if __name__ == '__main__':
    main()
