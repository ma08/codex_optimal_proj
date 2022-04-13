#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 11:06:38 2018
@author: ellenmacpherson
"""

import sys

def main():
    lines = sys.stdin.readlines()
    num_cases = int(lines[0])
    for i in range(num_cases):
        num_presents = int(lines[2 * i + 1])
        presents = [tuple(map(int, lines[2 * i + 2 + j].split())) for j in range(num_presents)]
        print("YES" if is_possible(presents) else "NO")

def is_possible(presents):
    presents.sort()
    for i in range(len(presents)):
        if presents[i][0] < i or presents[i][1] < i:
            return False
    return True

if __name__ == '__main__':
    main()
