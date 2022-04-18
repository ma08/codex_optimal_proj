#!/usr/bin/env python
# coding: utf-8

import math

L = int(input())

if L % 2 == 0:
    a = L / 2.0
    b = L / 2.0
    c = L / 2.0
else:
    a = (L - math.sqrt(L)) / 2.0
    b = (L + math.sqrt(L)) / 2.0
    c = L / 2.0

print(a * b * c)
