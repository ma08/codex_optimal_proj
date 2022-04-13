#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    a, b = sys.stdin.readline().strip().split(' ')
    for i, c in enumerate(b):
        if b[i] in a:
            for j in range(i):  # 前
                print('.' * len(a))
            print(a)
            for j in range(i+1, len(b)):  # 後
                print('.' * len(a))
            break

if __name__ == "__main__":
    main()
