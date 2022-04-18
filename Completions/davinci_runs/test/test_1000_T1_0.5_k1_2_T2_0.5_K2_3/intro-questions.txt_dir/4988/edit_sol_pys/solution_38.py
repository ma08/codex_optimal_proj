#!/usr/bin/env python3

import sys

def factorial(n):
    if n == 0:
        return 1 % 10
    else:
        return (n * factorial(n-1)) % 10

def main():
    for i in range(int(sys.stdin.readline())):
        print(factorial(int(sys.stdin.readline()) % 10))

main()
