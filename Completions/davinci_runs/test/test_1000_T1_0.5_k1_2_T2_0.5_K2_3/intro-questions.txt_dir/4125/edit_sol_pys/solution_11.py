

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:55:03

import sys

def solve(x, xs):
    xs = sorted(xs.items(), key=lambda x: x[1])
    x_min, x_max = xs[0], xs[-1]
    if x < x_min or x > x_max:
        return x_max - x_min
    else:
        return min(x - x_min, x_max - x)

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = dict(zip(list(range(1, n + 1)), map(int, sys.stdin.readline().split())))
    print(solve(x, xs))

if __name__ == '__main__':
    main()
