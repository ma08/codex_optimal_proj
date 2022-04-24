
# coding: utf-8

from sys import stdin
from math import sqrt

def is_int(x):
    return int(x) == x

N = int(stdin.readline())

if is_int(sqrt(N)):
    print("Yes")
else:
    print("No")
