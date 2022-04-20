

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:50:58

import sys

def solve(xs):
    xs = sorted(xs)
    x_min = xs[0]
    x_max = xs[-1]
    return x_max - x_min + 1

def main():
    n = int(sys.stdin.readline())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(x, xs))

if __name__ == '__main__':
    main()
