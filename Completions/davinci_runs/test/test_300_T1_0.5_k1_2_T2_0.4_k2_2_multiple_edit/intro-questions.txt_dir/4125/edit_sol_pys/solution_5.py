

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-14 16:49:37
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-14 16:54:41

import sys

def solve(x, xs):
    xs = sorted(xs) # sort the list
    x_min, x_max = xs[0], xs[-1] # get the min and max elements
    if x < x_min: # if x is smaller than all elements in xs
        x_max = x_max + (x_min - x) # move x_max to the right
    elif x > x_max: # if x is larger than all elements in xs
        x_min = x_min - (x - x_max) # move x_min to the left
    return x_max - x_min # return the distance between x_min and x_max

def main():
    n, x = map(int, sys.stdin.readline().split())
    xs = list(map(int, sys.stdin.readline().split()))
    print(solve(x, xs))

if __name__ == '__main__':
    main()
