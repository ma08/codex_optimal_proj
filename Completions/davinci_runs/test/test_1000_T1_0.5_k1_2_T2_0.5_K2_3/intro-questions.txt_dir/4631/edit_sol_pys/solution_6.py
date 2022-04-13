#!/usr/bin/env python3

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))
    x.sort()
    y = [0] * m
    for i in range(m):
        y[i] = x[i % n]
        x[i % n] += 1
    print(sum(y), ' '.join(map(str, y)), sep='\n')


if __name__ == "__main__":
    main()
