#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    k, x = [int(i) for i in sys.stdin.readline().split()]

    if (500 * k) >= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
