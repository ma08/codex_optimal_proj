# -*- coding: utf-8 -*-

import sys


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        for j in range(a[i]):
            b[i] += (j + 1) * (a[i] - j)
    print(sum(b))


if __name__ == '__main__':
    main()
