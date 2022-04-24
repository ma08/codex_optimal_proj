#coding: utf-8

from sys import stdin
from math import sqrt, floor, ceil

def isInt(x):
    return ceil(x) == x

N = int(stdin.readline())

if isInt(sqrt(N)):
    print("Yes")
else:
    print("No")
