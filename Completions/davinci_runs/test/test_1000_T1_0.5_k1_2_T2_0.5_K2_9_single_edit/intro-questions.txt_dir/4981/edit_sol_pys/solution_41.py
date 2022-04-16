#!/usr/bin/env python3

import sys

def main():
    numbers = sys.stdin.readline().strip().split()
    numbers = [int(i) for i in numbers]
    order = sys.stdin.readline().strip().split()
    numbers = sorted(numbers)
    for i in order: print(numbers.pop(0), end=' ')

main()
