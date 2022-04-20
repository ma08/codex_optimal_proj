
# -*- coding: utf-8 -*-
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    b = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    for i in range(n):
        print(' '.join(str(sum(a[i][k]*b[k][j] for k in range(m))) for j in range(m)))
if __name__ == "__main__":
    main()
