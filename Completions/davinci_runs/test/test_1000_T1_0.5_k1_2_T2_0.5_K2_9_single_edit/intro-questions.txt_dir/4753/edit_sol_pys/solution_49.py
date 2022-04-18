#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def solve(n):
    return n*(n-3)//2 if n>=3 else 0

def main():
    n = int(sys.stdin.readline())
    print(solve(n))

if __name__ == '__main__':
    main()
