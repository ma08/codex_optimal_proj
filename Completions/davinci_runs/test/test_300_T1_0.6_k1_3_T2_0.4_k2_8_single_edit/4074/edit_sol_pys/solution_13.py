#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 19:09:13 2019

@author: abhijithneilabraham
"""

def divisible(n,k):
    if n%k == 0:
        return n//k
    else:
        return n//k + 1

t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    print(divisible(n,k))
