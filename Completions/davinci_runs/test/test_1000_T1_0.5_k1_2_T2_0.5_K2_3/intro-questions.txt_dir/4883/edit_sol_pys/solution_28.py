#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    m, n = map(int, sys.stdin.readline().split())
    codes = {}
    for i in range(m):
        line = sys.stdin.readline().split()
        codes[line[0]] = line[1]
    for i in range(n):
        line = sys.stdin.readline().split()
        if translate(line[0], codes) == translate(line[1], codes): # compare translated strings
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
