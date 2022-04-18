#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().split()
    a = [int(x) for x in a]
    i = 0
    stairways = 0
    steps = []
    while i < n:
        stairways += 1
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        steps.append(a[i])
        i = j
    print(stairways)
    print(*steps)

if __name__ == '__main__':
    main()
