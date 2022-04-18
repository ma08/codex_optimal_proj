#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:18:22 2019
@author: y56
"""

import sys

def main():
    N = int(sys.stdin.readline())
    rods = []
    for i in range(N):
        rods.append(int(sys.stdin.readline()))
    rods.sort(reverse = True)
    while len(rods) > 1:
        rods.append(rods.pop() + rods.pop() - 1)
        rods.sort()
    print(rods[0])

if __name__ == '__main__':
    main()
