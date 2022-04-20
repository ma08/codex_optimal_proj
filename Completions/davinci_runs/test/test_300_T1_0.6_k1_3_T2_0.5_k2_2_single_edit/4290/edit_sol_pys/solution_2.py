#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:42:02 2019
@author: jinlingxing
"""

import sys

def solve(n, m):
    return n * m 

def main():
    lines = sys.stdin.readlines()
    n,m = map(int, lines[0].strip().split())
    print(solve(n,m))


if __name__ == '__main__':
    main()
