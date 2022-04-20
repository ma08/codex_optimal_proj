#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:39:38 2019

@author: xsxsz
"""


def solve(n, a):
    max_len = 1
    curr_len = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            curr_len += 1
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1
    return max(max_len, curr_len)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
