#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-08 15:30:41
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-08 15:35:08

import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return a*b//gcd(a, b)

def main():
    lines = [line.strip() for line in sys.stdin]

    for i, line in enumerate(lines[1:], 1):
        n, shuffle = line.split()
        n, shuffle = int(n), shuffle[0]
        if shuffle == 'o':
            print(i, lcm(n//2, n//2+1)//(n//2))
        else:
            print(i, lcm(n//2, n//2-1)//(n//2))

if __name__ == '__main__':
    main()
