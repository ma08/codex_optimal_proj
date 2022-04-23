#!/usr/bin/env python3
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    survivors = set([i for i in range(1, n+1)])
    for _ in range(k):
        d = int(sys.stdin.readline())
        survivors -= set(map(int, sys.stdin.readline().split()))
    print(len(survivors))

if __name__ == '__main__':
    main()
