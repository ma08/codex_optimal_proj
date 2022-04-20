#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13
# @Author  : Edrain

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append((a[i] + b[i]) % n)
    c.sort()
    for i in range(n):
        print(c[i], end=' ')

if __name__ == '__main__':
    main()
