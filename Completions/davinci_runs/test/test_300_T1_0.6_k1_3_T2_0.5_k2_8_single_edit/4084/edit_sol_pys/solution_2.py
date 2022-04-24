#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'maximus'

n, a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd = gcd(a, b)

print((n // (a + b) * a + min(n % (a + b), a)) % gcd)
