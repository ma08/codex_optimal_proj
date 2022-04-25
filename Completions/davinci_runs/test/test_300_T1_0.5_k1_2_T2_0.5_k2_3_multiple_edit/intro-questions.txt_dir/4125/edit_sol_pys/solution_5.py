

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:54:35

import sys

def solve(n, x, xs):
    xs = sorted(xs, reverse=True)
    if xs[0] < x:
        x = xs[0]
    return sum([x - x_i for x_i in xs])

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(n, x, xs))

if __name__ == '__main__':
    main()
