#!/usr/bin/env python3

import sys
import random

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    while len(a) > 1:
        i = random.randint(0, len(a)-1)
        j = random.randint(0, len(a)-1)
        if i == j:
            continue
        a[i] -= a[j]
        if a[i] <= 0:
            a.pop(i)
        if a[j] <= 0:
            a.pop(j)
    print(a[0])

if __name__ == "__main__":
    main()
