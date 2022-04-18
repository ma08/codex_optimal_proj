#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    i = 0
    stairways_count = 0
    steps = []
    while i < n:
        stairways_count += 1
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        steps.append(a[i])
        i = j
    print(stairways_count)
    print(*steps)

if __name__ == '__main__':
    main()
