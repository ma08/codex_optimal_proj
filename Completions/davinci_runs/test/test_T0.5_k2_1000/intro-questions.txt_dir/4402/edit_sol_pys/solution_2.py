#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A - 年齢
"""

A, B = map(int, input().split())

if A >= 13:
    print(B)
elif A >= 6:
    print(B // 2)
else:
    print(0)
