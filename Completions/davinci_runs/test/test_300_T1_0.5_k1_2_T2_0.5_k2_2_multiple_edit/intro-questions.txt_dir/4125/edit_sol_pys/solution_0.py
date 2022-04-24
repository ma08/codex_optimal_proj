

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 17:12:18

import sys

def solve(x, xs):
    xs = sorted(xs)
    min_x = xs[0]
    max_x = xs[-1]
    if x < min_x:
        max_x = max_x + (min_x - x)
    elif x > max_x:
        min_x = min_x - (x - max_x)
    return max_x - min_x

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(x, xs))

if __name__ == '__main__':
    main()
