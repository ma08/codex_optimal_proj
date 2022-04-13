

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:56:10

import sys

def solve(x, xs):
    xs = sorted(xs)
    x_min, x_max = xs[0], xs[-1] 
    if x <= x_min or x >= x_max:
        return x_max - x_min 
    else:
        return min(x - x_min, x_max - x) 

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(x, xs))

if __name__ == '__main__':
    main()
