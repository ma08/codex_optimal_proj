#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-08-08 20:37:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = 1
    for t in T:
        ans = lcm(ans, t)
    print(ans)

if __name__ == '__main__':
    main()
