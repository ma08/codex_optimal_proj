#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from random import randint


def solve(n, m, s, d, c, p):
    # Write your code here
    # return a list of length s with your solution
    return [randint(1, n) for _ in range(s)]

lines = sys.stdin.readlines()
n, m, s, d = map(int, lines[0].split())
c = map(int, lines[1].split())
p = map(int, lines[2].split())

res = solve(n, m, s, d, c)
if res == None:
    print("impossible") # if the solution is impossible, print "impossible"
else:
    print(" ".join([str(x) for x in res]))
