#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:54:28 2019

@author: nishanth
"""

# Getting input
M, N = [int(x) for x in input().split()]  # M = no of rows, N = no of columns
U, L, R, D = [int(x) for x in input().split()]  # U = no of rows above, L = no of columns on left, R = no of columns on right, D = no of rows below

# Creating the crossword
crossword = [input() for x in range(M)]  # crossword = list of rows

# Creating the frame
frame = []
for i in range(U):
    frame.append("#."*(N+L+R-1)+"#")
frame.append("."*L+crossword[0]+"."*R)
for i in range(1,M):
    frame.append("."*L+crossword[i]+"."*R)
for i in range(D):
    frame.append("#."*(N+L+R-1)+"#")

# Printing the frame
for line in frame:
    print(line)
