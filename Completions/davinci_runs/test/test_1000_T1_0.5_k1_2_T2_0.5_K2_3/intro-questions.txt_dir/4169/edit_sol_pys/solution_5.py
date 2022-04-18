#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/10 下午5:14
# @Author  : Hou Rong
# @Site    : 
# @File    : file
# @Software: PyCharm



def main():
    N, M = [int(x) for x in input().split()]
    price_list = []  # 存放价格和数量的列表
    for i in range(N):
        price_list.append([int(x) for x in input().split()])
    price_list.sort()  # 按照价格排序
    total = 0
    while M > 0:
        if price_list[0][1] >= M:
            total += price_list[0][0] * M
            M = 0
        else:
            total += price_list[0][0] * price_list[0][1]
            M -= price_list[0][1]
            price_list.pop(0)
    print(total)

if __name__ == '__main__':
    main()
