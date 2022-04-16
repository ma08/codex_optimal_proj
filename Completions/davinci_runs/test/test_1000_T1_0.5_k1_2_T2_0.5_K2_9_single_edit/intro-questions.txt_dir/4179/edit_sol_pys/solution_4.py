#!/usr/bin/env python3

import sys

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]
    count = 0
    for i in range(n):
        if sum(a[i][j] * b[j] for j in range(m)) + c > 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
