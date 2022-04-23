

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:53:10

import sys

def solve(xs, x):
    x_min = min(xs)
    x_max = max(xs)
    if x < x_min:
        x_max = x_max + (x_min - x)
    elif x > x_max:
        x_min = x_min - (x - x_max)
    return x_max - x_min

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(xs, x))

if __name__ == '__main__':
    main()
