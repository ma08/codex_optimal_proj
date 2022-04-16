#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
if N == 1:
    print("Hello World")
else:
    A, B = map(int, input().split())
    print(A + B)
