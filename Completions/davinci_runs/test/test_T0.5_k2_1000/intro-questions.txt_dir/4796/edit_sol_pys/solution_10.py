#!/usr/bin/env python3

import sys
import math

def get_input():
    A, B, C = map(int, sys.stdin.readline().split())
    I, J, K = map(int, sys.stdin.readline().split())
    return A, B, C, I, J, K

def get_leftovers(A, B, C, I, J, K):
    max_cocktails = min(A/I, B/J, C/K) if I != 0 and J != 0 and K != 0 else 0
    return A - max_cocktails*I, B - max_cocktails*J, C - max_cocktails*K

def main():
    A, B, C, I, J, K = get_input()
    A, B, C = get_leftovers(A, B, C, I, J, K)
    print("%.6f %.6f %.6f" % (A, B, C))

if __name__ == "__main__":
    main()
