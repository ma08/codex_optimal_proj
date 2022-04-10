#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 00:00:00 2018

@author: kkrista
"""


def main():
    n = int(input())
    seq = []
    for i in range(n):
        line = [int(x) for x in input().split()]
        seq.append(line)
    seq.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n):
        if i == 0:
            ans = max(ans, seq[i+1][0] - seq[i][1])
        elif i == n-1:
            ans = max(ans, seq[i][0] - seq[i-1][1])
        else:
            ans = max(ans, seq[i][0] - seq[i-1][1])
            ans = max(ans, seq[i+1][0] - seq[i][1])
    print(ans)


if __name__ == '__main__':
    main()
