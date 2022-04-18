#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    read_line = sys.stdin.readline
    C, n = map(int, read_line().split())
    passengers = [0]
    for _ in range(n):
        left, entered, waited = map(int, read_line().split())
        passengers.append(passengers[-1] + entered - left + waited)
    print("possible" if all(0 <= x <= C for x in passengers) else "impossible")

if __name__ == '__main__':
    main()
