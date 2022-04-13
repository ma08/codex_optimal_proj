#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 17:28:09 2019
@author: yanying
"""
n = int(input())
a = [int(i) for i in input().split()]
b = [i for i in a if i != -1]
print(sum(b)/len(b))
