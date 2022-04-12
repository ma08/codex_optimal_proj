#!/usr/bin/env python3

import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def euler(n):
    e = 0
    for i in range(0, n+1): # range(0, n+1) is equivalent to range(n+1)
        e += 1 / factorial(i)
    return e

def main():
    n = int(sys.stdin.readline().strip()) # read the first line
    print(euler(n))

if __name__ == '__main__':
    main()
