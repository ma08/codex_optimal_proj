import sys
import os
from collections import deque
from collections import Counter
from math import sqrt, hypot, factorial, pi, sin, cos, radians, log10
from heapq import heappop, heappush, heapify, heappushpop
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from functools import reduce, partial
from fractions import Fraction
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, bisect_right
from fractions import gcd
from random import randrange, randint

def read_list(t): return [t(x) for x in input().split()]
def read_line(t): return t(input())
def read_lines(t, N): return [t(input()) for _ in range(N)]

compose = lambda *funcs: reduce(lambda f, g: lambda *x: f(g(*x)), funcs)

def solve():
    n, m = read_list(int)
    foods = [0] * m
    for i in range(n):
        k = read_list(int)[0]
        for j in read_list(int):
            foods[j-1] += 1
    return foods.count(n)


def main():
    for _ in range(int(input())):
        print(solve())

if __name__ == '__main__':
    main()
