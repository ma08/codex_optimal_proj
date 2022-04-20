# -*- coding: utf-8 -*-

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    d = list(map(int, sys.stdin.readline().split()))
    print(a[0] + b[0])

if __name__ == '__main__':
    main()
