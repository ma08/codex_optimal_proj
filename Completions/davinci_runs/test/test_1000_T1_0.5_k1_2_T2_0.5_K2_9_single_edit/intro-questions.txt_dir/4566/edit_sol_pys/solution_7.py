#!/usr/bin/python
# -*- coding: utf-8 -*-

n, m = map(int, input().split())

# 入力
roads = []
for i in range(m):
    a, b = map(int, input().split())  # スペース区切り
    roads.append([a, b])

# 出力
for i in range(1, n+1):
    count = 0
    for road in roads:
        if i in road:
            count += 1
    print(count)
