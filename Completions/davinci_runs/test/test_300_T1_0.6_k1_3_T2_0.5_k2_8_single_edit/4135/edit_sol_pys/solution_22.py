#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:37:17 2019

@author: altsai
"""





# SOLUTION

n = int(input())
t = input()

s = [0]*n

for i in range(n-1, 0, -1):
  x = n//i
  y = n%i
  if y==0:
    for j in range(x):
      s[i*j] = t[i*(x-1-j)]
  else:
    for j in range(x+1):
      s[y+i*j] = t[y+i*(x-j)]

print(''.join(s))
