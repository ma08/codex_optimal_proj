#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 14:14:01 2020

@author: daniel
"""



n = int(input())

strings = []

for i in range(n):
    strings.append(input())

strings.sort(key=len)

for i in range(n):
    for j in range(i+1, n):
        if strings[i] in strings[j]:
            break
    else:
        print("NO")
        break
else:
    print("YES")
    for string in strings:
        print(string)
