#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 下午6:03
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : test.py

import sys

def main():
    n, x = map(int, sys.stdin.readline().split())
    x_lst = [int(i) for i in sys.stdin.readline().split()]
    x_lst.sort()

    if x in x_lst:
        x_lst.remove(x)

    min_d = max(x_lst[0] - x, x - x_lst[-1])
    for i in range(1, n):
        min_d = max(min_d, (x_lst[i] - x_lst[i - 1]) // 2)

    print(min_d)

if __name__ == '__main__':
    main()
