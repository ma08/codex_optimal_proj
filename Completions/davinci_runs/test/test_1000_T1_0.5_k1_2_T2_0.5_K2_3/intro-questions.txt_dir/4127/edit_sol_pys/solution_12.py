#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    a, b = map(float, sys.stdin.readline().split())
    print(int(a * b))

if __name__ == '__main__':
    main()
