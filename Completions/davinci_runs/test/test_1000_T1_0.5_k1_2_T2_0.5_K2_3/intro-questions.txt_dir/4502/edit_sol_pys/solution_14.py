#!/usr/bin/env python3

import sys

n = int(input())
a = list(map(int, input().split()))

stack = []
for i in range(n):
    stack.append(a[i])
    for j in range(len(stack)):
        print(stack[j], end=' ')
    print()
