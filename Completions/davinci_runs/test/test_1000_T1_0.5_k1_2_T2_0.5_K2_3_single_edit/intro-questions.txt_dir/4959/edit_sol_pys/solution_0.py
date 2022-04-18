#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 15:21
# @Author  : liuhu
# @File    : file
# @Software: PyCharm
# @github  :https://github.com/Max-Liuhu


a = map(int, raw_input().split())
soda = 0
empty = a[0] + a[1]
while empty >= a[2]:
    empty = empty - a[2] + 1
    soda += 1
print soda
