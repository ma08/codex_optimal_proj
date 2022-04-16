#!/usr/bin/env python3

import sys

def main():
    s, t = map(int, sys.stdin.readline().split())
    print(t-s+1)

if __name__ == "__main__":
    main()
