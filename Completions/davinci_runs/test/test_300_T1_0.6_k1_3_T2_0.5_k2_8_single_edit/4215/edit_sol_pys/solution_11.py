#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:10:25 2020
@author: zhangzhaopeng
@QQ: 1198744808
@blog: https://blog.csdn.net/qq_44226094
"""

A, B = map(int, input().split())
print(A - B if B < A else 0)
