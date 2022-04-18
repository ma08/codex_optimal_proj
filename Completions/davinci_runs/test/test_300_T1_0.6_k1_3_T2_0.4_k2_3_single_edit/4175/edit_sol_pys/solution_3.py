#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:48:08 2020

@author: hanpeng
"""


n = int(input())
words = [input() for i in range(n)]

for i in range(1,n):
    if words[i] in words[:i] or words[i][0] != words[i-1][-1]:
        print("No")
        exit()

print("Yes")
