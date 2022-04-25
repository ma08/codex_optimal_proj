

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:55:59

import sys

def solve(x, xs): # x is the center
    if len(xs) == 0:
        return 0
    else:
        xs = sorted(xs)
        x_min = x_max = xs[0]
        for x_i in xs:
            if x_i < x_min:
                x_min = x_i
            if x_i > x_max:
                x_max = x_i
        if x < x_min: # move x_min to x
            x_max = x_max + (x - x_min)
            x_min = x
        elif x > x_max: # move x_max to x
            x_min = x_min - (x - x_max)
            x_max = x
        return x_max - x_min

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(x, xs))

if __name__ == '__main__':
    main()
