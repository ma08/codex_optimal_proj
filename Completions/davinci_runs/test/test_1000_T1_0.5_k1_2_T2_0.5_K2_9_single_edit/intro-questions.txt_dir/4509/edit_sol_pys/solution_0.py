#!/usr/bin/env python3

import sys

def main():
    n = int(input())
    for _ in range(n):
        n, k = map(int, input().split())
        print(n * k + 1)

if __name__ == '__main__':
    main()
