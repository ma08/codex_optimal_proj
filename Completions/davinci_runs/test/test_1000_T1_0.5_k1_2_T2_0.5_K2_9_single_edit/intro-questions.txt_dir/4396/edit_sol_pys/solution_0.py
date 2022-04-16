# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    sum = 0
    for i in range(n):
        x, u = input().split()
        if u == 'JPY':
            sum += float(x)
        else:
            sum += float(x) * 380000.0
    print(sum)
    return

if __name__ == '__main__':
    main()
