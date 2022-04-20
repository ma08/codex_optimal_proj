#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

def input():
    return sys.stdin.readline()

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------

N = int(input())

if N == 1:
    print("Not Prime")
elif N == 2:
    print("Prime")
else:
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
