#!/usr/bin/env python


import sys, math

def get_min_cost(n, c):
    if n == 1:
        return 0
    min_cost = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            min_cost = min(min_cost, c[i]) + min_cost
            min_cost = min(min_cost, c[n//i]) + min_cost
    return min_cost

def get_min_split(n, c):
    if n == 1:
        return 1
    min_split = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            min_split = min(min_split, c[i]) + min_split
            min_split = min(min_split, c[n//i]) + min_split
    return min_split

def get_min_cost(n, c):
    if n == 1:
        return 0
    min_cost = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            min_cost = min(min_cost, c[i]) + min_cost
            min_cost = min(min_cost, c[n//i]) + min_cost
    return min_cost

def get_min_split(n, c):
    if n == 1:
        return 1
    min_split = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            min_split = min(min_split, c[i]) + min_split
            min_split = min(min_split, c[n//i]) + min_split
    return min_split
