#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :



N, M = map(int, input().split())

# 各頂点の次数を格納する辞書
degree = {}

for i in range(M):
    a, b = map(int, input().split())
    # 次数を計算する
    if a in degree:
        degree[a] += 1
    else:
        degree[a] = 1
    if b in degree:
        degree[b] += 1
    else:
        degree[b] = 1

# 次数を出力する
for i in range(N):
    if i + 1 in degree:
        print(degree[i + 1])
    else:
        print(0)
