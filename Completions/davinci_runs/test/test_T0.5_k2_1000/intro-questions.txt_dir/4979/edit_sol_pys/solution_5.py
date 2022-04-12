#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    print(int(bin(n)[2:][::-1], 2), end="")

if __name__ == "__main__":
    main()
