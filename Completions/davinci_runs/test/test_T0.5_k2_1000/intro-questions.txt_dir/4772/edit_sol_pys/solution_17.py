
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:46:07 2019

@author: abhijithneilabraham
"""


R, C = map(int, input().split())
crossword = []
for i in range(R):
    crossword.append(list(input()))

def check_horizontal(crossword, R, C):
    for r in range(R):
        for c in range(C - 1):
            if crossword[r][c].isalpha() and crossword[r][c + 1].isalpha():
                return True
    return False

def check_vertical(crossword, R, C):
    for c in range(C):
        for r in range(R - 1):
            if crossword[r][c].isalpha() and crossword[r + 1][c].isalpha():
                return True
    return False

def get_horizontal(crossword, R, C):
    for r in range(R):
        for c in range(C - 1):
            if crossword[r][c].isalpha() and crossword[r][c + 1].isalpha():
                return crossword[r][c] + crossword[r][c + 1]

def get_vertical(crossword, R, C):
    for c in range(C):
        for r in range(R - 1):
            if crossword[r][c].isalpha() and crossword[r + 1][c].isalpha():
                return crossword[r][c] + crossword[r + 1][c]

if check_horizontal(crossword, R, C):
    print(get_horizontal(crossword, R, C))
else:
    print(get_vertical(crossword, R, C))
