#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:10:34 2020

@author: nenad
"""


"""
Problem description: https://codeforces.com/problemset/problem/1294/A
"""
import sys


def solve(n, m):
    if n == 1:
        return 0
    elif n == 2:
        return m
    else:
        return (m - n + 1) * 2


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        print(solve(n, m))
