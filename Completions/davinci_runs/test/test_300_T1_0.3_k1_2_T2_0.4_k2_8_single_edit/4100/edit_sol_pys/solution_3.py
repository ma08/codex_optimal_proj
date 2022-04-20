#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-27 13:55:08
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-27 13:55:08

n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]

players = [k] * n

for i in range(q):
    for j in range(n):
        if j + 1 != a[i]:
            players[j] -= 1

for i in range(n):
    if players[i] <= 0:
        print("No")
    else:
        print("Yes")
