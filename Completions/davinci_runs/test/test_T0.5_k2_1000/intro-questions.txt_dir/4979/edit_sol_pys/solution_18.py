#!/usr/bin/env python

import sys

def reverse_binary_number(n):
    return int(bin(n)[2:][::-1], 2)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    print(reverse_binary_number(n))
