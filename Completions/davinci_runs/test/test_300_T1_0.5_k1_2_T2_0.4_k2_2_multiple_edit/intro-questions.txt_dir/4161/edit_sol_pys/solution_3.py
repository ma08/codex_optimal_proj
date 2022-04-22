#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

K = int(sys.stdin.readline())


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def gcd3(x, y, z):
    return gcd(gcd(x, y), z)


def main():
    print(sum([gcd3(a, b, c) for a in range(1, K+1) for b in range(1, K+1) for c in range(1, K+1)]))

main()
