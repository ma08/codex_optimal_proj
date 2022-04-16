#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/8 11:02
# @Author  : tanxw
# @Desc    : 列表解析

import sys

    """
    输入：
    5
    2 3 4 5 6
    输出：
    2 4
    """
def main():
    n = int(sys.stdin.readline().strip())
    temp = [int(i) for i in sys.stdin.readline().strip().split()]
    max_temp = []
    for i in range(len(temp) - 2):
        max_temp.append(max(temp[i], temp[i+1], temp[i+2]))
    index = max_temp.index(min(max_temp))
    print(index + 1, max_temp[index])


if __name__ == '__main__':
    main()
