#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 20:47:01 2020

@author: suryakantkumar
"""


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a, b, c = [int(x) for x in input().split()]

g = gcd(gcd(a, b), c)

print(min(a//g, b//g, c//g)*7)
