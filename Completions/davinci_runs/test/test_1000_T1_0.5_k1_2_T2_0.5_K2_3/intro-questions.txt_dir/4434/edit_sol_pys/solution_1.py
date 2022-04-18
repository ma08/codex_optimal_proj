#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_input():
    t = int(raw_input())
    for i in range(t):
        n = int(raw_input())
        yield n

def solve(n):
    if n == 1:
        return 0
    return (n - 1)**2

if __name__ == '__main__':
    for n in get_input():
        print(solve(n))
