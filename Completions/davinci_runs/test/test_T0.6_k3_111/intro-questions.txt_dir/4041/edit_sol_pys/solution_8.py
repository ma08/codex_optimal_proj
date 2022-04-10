#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-22 10:04:47
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-22 10:05:58

import sys

def subsequence(s, t):
    m = len(s)
    n = len(t)
    l = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif s[i-1] == t[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])
    return l[m][n]

def main():
    reader = (line.strip() for line in sys.stdin)
    s, t = next(reader), next(reader)
    print(len(s) - subsequence(s, t))

if __name__ == "__main__":
    main()
