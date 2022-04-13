#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:22:43 2019

@author: michaelboles
"""

# set up grid
n = int(input())

grid = []
for _ in range(n):
    grid.append(input())

# check for the same number of black and white squares in each row and column
row_count = []
col_count = []
for i in range(n):
    row_count.append(grid[i].count('B'))
    col_count.append(0)
    for j in range(n):
        col_count[i] += 1 if grid[j][i] == 'B' else 0

# check for adjacent squares of the same color
for i in range(n):
    if grid[i].count('BBB') > 0 or grid[i].count('WWW') > 0:
        print(0)
        exit()
    for j in range(n-2):
        if grid[i][j] == grid[i][j+1] and grid[i][j] == grid[i][j+2]:
            print(0)
            exit()

# check for the same number of black and white squares in each row and column
for i in range(n):
    if row_count[i] != n//2:
        print(0)
        exit()
    if col_count[i] != n//2:
        print(0)
        exit()

print(1)
