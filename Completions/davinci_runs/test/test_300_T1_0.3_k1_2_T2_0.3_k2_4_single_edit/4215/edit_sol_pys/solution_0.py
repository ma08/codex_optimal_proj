#!/usr/bin/env python

import sys

def main():
    a, b = map(int, sys.stdin.readline().split())  # read a line with a split
    print(a - b)  # print the output

if __name__ == "__main__":
    main()
