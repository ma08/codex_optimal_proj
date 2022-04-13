#!/usr/bin/env python3

import sys
sys.stdin = open('input.txt', 'r')

q = int(input())
for _ in range(q):
    n = int(input())
    a = list(map(int, input().split())) #list of ints
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i] #swap
            break
    print(*a)
