#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

N = int(sys.stdin.readline())

if N**0.5 == int(N**0.5):
    print("Yes")
else:
    print("No")
