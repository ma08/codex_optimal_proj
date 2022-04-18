#!/usr/bin/env python3

import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    print(n * m)

if __name__ == "__main__":
    main()
