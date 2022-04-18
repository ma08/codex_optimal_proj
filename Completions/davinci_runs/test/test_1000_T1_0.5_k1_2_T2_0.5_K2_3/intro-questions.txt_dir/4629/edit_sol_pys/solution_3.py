#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:13:04 2019

@author: abhijithneilabraham
"""

def func():
    n=int(input())
    l=[]
    for i in range(n):
        l.append(int(input()))
    l.sort()
    for i in l:
        print(i)
func()
