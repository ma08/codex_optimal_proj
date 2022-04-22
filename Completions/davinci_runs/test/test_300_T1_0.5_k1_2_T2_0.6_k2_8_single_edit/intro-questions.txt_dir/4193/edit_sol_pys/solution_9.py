#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import math


def main():
    input_str = sys.stdin.readline()
    S, T = input_str.split()
    A, B = sys.stdin.readline().split()
    U = sys.stdin.readline()
    A = int(A)
    B = int(B)
    if S == U:
        print(A-1, B)
    else:
        print(A, B-1)

if __name__ == "__main__":
    main()


import sys

def main():
    # read input
    N = int(sys.stdin.readline())
    for i in range(N):
        s = sys.stdin.readline()
        print(s)

if __name__ == "__main__":
    main()
