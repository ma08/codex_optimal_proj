#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:37:30 2020

@author: j-bd
"""

import sys

def area(point_a, point_b, point_c):
    """Compute the area of a triangle"""
    return abs(point_a[0]*(point_b[1] - point_c[1]) + point_b[0]*(point_c[1] - point_a[1]) + point_c[0]*(point_a[1] - point_b[1]))/2

def contains(point_a, point_b, point_c, point_p):
    """Check if a point is in a triangle"""
    return area(point_a, point_b, point_c) == area(point_a, point_b, point_p) + area(point_a, point_p, point_c) + area(point_p, point_b, point_c)

POINT_A = tuple(map(int, sys.stdin.readline().split()))
POINT_B = tuple(map(int, sys.stdin.readline().split()))
POINT_C = tuple(map(int, sys.stdin.readline().split()))

NUMBER_POINTS = int(sys.stdin.readline())

COUNT = 0
for _ in range(NUMBER_POINTS):
    POINT_P = tuple(map(int, sys.stdin.readline().split()))
    if contains(POINT_A, POINT_B, POINT_C, POINT_P):
        COUNT += 1

print("%.1f" % area(POINT_A, POINT_B, POINT_C))
print(COUNT)
