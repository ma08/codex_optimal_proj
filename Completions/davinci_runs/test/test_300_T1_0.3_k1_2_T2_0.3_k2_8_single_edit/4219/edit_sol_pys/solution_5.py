#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import sys

def input():
    return sys.stdin.readline().strip()

def solve(people):
    N = len(people)
    for i in range(N):
        for j in range(i+1, N):
            if is_consistent(people[i], people[j]):
                return 2
    return 1

def is_consistent(person1, person2):
    for x_i1, y_i1 in person1:
        for x_i2, y_i2 in person2:
            if x_i1 == x_i2 and y_i1 != y_i2:
                return True
    return False

if __name__ == '__main__':
    main()
