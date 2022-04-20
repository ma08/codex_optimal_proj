#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
import sys
a, b, c, k = map(int, sys.stdin.readline().split())

if k <= a:
    print(k)
elif k <= a + b:
    print(a)
else:
    print(a - (k - a - b))
