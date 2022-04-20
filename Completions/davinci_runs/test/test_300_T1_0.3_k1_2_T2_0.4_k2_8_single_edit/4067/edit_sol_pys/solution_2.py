#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    print(s[::-1])

if __name__ == '__main__':
    main()
