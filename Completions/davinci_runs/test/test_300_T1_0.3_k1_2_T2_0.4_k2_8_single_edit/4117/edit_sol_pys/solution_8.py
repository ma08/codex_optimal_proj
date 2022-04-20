#!/usr/bin/env python3

import sys

N = int(input())
L = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] != L[j] and L[j] != L[k] and L[k] != L[i]:
                if L[i] + L[j] > L[k] and L[j] + L[k] > L[i] and L[k] + L[i] > L[j]:
                    count += 1

print(count)
