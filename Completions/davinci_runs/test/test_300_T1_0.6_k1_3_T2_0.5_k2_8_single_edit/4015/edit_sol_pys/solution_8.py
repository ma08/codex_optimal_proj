#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:46:31 2020

@author: karanwaghela
"""

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































n, m = map(int, input().split())

if n == m:
    print(0)
    quit()

if m % 2 == 1 and m % 3 == 1:
    print(-1)
    quit()

steps = 0

while n != 1:
    if n % 3 == 0:
        n = int(n / 3)
    elif n % 2 == 0:
        n = int(n / 2)
    else:
        print(-1)
        quit()
    steps += 1

while m != 1:
    if m % 3 == 0:
        m = int(m / 3)
    elif m % 2 == 0:
        m = int(m / 2)
    else:
        print(-1)
        quit()
    steps += 1

print(steps)
