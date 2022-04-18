#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    temperatures = sorted(list(map(int, sys.stdin.readline().split())))
    print(temperatures)

if __name__ == "__main__":
    main()
