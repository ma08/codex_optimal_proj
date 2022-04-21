#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:04:58 2020
"""

import math

def minPowerStrips(A, B):
    return math.ceil(B / A)

def main():
    line = input().split()
    A = int(line[0])
    B = int(line[1])
    print(minPowerStrips(A, B))

if __name__ == '__main__':
    main()
