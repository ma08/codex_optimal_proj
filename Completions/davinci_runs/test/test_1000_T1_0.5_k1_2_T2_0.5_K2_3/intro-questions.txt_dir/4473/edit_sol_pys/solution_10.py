#!/usr/bin/env python3

import sys

def main():
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        a, b, k = map(int, sys.stdin.readline().split())
        if k % 2:
            print(a * (k // 2) - b * (k // 2 + 1), end=' ')
        else:
            print(a * (k // 2) - b * (k // 2), end=' ')

if __name__ == "__main__":
    main()
