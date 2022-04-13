#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys

def main():
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().split()
    a = [int(x) for x in a]
    i = 0
    stairways_count = 0
    steps = [0]
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        steps.append(j - i)
        i = j
    print(len(steps))
    print(*steps)

if __name__ == '__main__':
    main()
