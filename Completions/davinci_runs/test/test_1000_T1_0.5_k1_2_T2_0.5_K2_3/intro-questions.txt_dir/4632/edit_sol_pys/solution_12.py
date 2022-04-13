#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 11:06:38 2018
@author: ellenmacpherson
"""
"""
Given a list of packages with weight and value, determine if it is possible to make a package of weight w
"""
import sys

def main():
    lines = sys.stdin.readlines()
    num_cases = int(lines[0])
    for i in range(num_cases):
        num_packages = int(lines[2 * i + 1])
        packages = [tuple(map(int, lines[2 * i + 2 + j].split())) for j in range(num_packages)] # split into tuples
        print("YES" if is_possible(packages) else "NO") # check if possible

def is_possible(packages):
    packages.sort() # sort by weight
    for i in range(len(packages)):
        if packages[i][0] < i or packages[i][1] < i: # check if weight and value is less than index
            return False
    return True

if __name__ == '__main__':
    main()
