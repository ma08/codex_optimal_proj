#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 00:00:00 2018

@author: kkrista
"""


def main():
    n = int(input())
    seq = [0]
    for i in range(n):
        seq.append(int(input()))
    seq.append(10**9+1)
    seq.sort()
    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, seq[i+1] - seq[i])
        elif i == n-1:
            ans = max(ans, seq[i] - seq[i-1])
        else:
            ans = max(ans, seq[i] - seq[i-1])
            ans = max(ans, seq[i+1] - seq[i])
    print(ans)


if __name__ == '__main__':
    main()
