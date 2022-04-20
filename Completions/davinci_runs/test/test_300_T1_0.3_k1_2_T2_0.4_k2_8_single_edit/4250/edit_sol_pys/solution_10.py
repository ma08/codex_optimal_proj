#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline())
    a = []
    for i in range(n):
        a.append(list(map(int, sys.stdin.readline().split())))
    for i in range(n):
        for j in range(n):
            if i == j:
                a[i][j] = 0
            else:
                a[i][j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                a[i][j] = 0
        else:
    for i in range(n):
        print(*a[i])

if __name__ == '__main__':
    main()
