#!/usr/bin/env python3

import sys
import random

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    while len(A) > 1:
        i = random.randint(0, len(A)-1)
        j = random.randint(0, len(A)-1)
        if i == j:
            continue
        A[i] -= A[j]
        if A[i] <= 0:
            A.pop(i)
        if A[j] <= 0:
            A.pop(j)
    print(A[0])

if __name__ == "__main__":
    main()
