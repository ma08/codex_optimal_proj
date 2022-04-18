#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 16:52
# @Author  : 一叶知秋
# @File    : file.py
# @Software: PyCharm


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        if n == 1:
            print(0)
        else:
            print(max(2 * m - n, n - 2 * m))


if __name__ == '__main__':
    main()
