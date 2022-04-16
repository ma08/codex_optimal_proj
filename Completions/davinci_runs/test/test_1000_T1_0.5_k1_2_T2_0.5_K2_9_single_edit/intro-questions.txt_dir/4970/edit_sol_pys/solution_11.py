#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:03:42 2020
@author: xiaokewang
"""

import sys
import os

os.chdir('/Users/xiaokewang/Desktop/')










from collections import defaultdict

def main():
    frosh = int(sys.stdin.readline().strip())
    classes = defaultdict(lambda: 0)
    for _ in range(frosh):
        courses = tuple(sorted(map(int, sys.stdin.readline().strip().split())))
        classes[courses] += 1
    print(max(classes.values()))

if __name__ == "__main__":
    main()
