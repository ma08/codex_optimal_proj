#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/24 22:09
# @Author  : xingyuezhiji
# @Email   : zhong180@126.com
# @File    : test.py
# @Software: PyCharm
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = [0] * n
for i in range(n):
    c[(a[i] + b[i]) % n] += 1

for i in range(n):
    for j in range(c[i]):
        print(i, end=" ")
