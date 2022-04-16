#!/usr/bin/env python


import sys, os
from math import *

if len(sys.argv) < 2:
    print("Usage: ./file.py <input_file>")
    sys.exit(1)

def main():
    n, a = map(int, sys.stdin.readline().split())
    e = list(map(int, sys.stdin.readline().split()))
    e.sort()
    #print(e)
    count = 0
    for i in range(n):
        if a >= e[i]:
            count += 1
            a -= e[i]
        else:
            break
    print(count)

main()
