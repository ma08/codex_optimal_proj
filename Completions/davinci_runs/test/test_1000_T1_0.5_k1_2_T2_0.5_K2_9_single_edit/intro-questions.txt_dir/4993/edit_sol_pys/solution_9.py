#!/usr/bin/env python3

import sys

def main():
    P, N = map(int, sys.stdin.readline().split())
    parts = set()
    for i in range(N):
        part = sys.stdin.readline().strip()
        parts.add(part)
        if len(parts) == P:
            print(i + 1)
            return
    print('paradox avoided')

if __name__ == '__main__':
    main()
