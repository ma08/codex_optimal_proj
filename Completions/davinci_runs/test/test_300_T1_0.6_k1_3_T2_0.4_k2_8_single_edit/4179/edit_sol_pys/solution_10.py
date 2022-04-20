# coding: utf-8

import sys

def main():
    n, m, c = map(int, sys.stdin.readline().split())
    b = list(map(int, sys.stdin.readline().split()))
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    count = 0
    for i in range(n):
        total = 0
        for j in range(m):
            total += a[i][j] * b[j]
        if total + c > 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
