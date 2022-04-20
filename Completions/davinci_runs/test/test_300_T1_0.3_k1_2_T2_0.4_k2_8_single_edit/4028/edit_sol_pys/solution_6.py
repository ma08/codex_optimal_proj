#!/usr/bin/env python3

import sys

def get_input():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    return n, s

def solve(n, s):
    return n

def main():
    n, s = get_input()
    print(solve(n, s))

if __name__ == '__main__':
    main()
