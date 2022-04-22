

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:55:02

import sys

def solve(x, xs):
    xs = sorted(xs)
    x_min, x_max = xs[0], xs[-1]
    if x < x_min: # x < x_min, i.e. x is smaller than all elements in xs
        x_max = x_max + (x_min - x) # move x_max to the right
    elif x > x_max: # x > x_max, i.e. x is larger than all elements in xs
        x_min = x_min - (x - x_max) # move x_min to the left
    return x_max - x_min # return the distance between x_max and x_min

def main():
    _, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(x, xs))

if __name__ == '__main__':
    main()
