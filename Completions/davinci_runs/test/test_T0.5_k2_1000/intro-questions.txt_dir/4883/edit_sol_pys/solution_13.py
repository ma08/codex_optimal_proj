#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:06:13 2020

@author: krishna
"""

import sys

def main():
    m, n = map(int, sys.stdin.readline().split()) # read the first line
    codes = {}
    for i in range(m):
        line = sys.stdin.readline().split() # read the code line
        codes[line[0]] = line[1]
    for i in range(n):
        line = sys.stdin.readline().split() # read the word line
        if translate(line[0], codes) == translate(line[1], codes):
            print("yes")
        else:
            print("no")

def translate(word, codes):
    res = ""
    for char in word:
        if char in codes:
            res += codes[char]
        else:
            res += char
    return res

if __name__ == "__main__":
    main()
