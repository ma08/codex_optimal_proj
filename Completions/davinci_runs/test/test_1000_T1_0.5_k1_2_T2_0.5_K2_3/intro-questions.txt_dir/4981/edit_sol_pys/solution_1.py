#!/usr/bin/python

import sys

def main():
    inputs = [int(i) for i in sys.stdin.readline().strip().split()]
    order = sys.stdin.readline().strip()
    inputs = sorted(inputs)
    for i in order:
        print(inputs.pop(0), end=' ')

main()
