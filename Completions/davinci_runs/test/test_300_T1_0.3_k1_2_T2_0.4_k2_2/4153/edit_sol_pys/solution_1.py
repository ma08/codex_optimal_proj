#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Tao Yimin
# Time  :2019/10/31 11:04

N = int(input())
S = input()

# 0:red, 1:blue

# stack
stack = []

for i in range(N):
    if len(stack) == 0:
        stack.append(S[i])
    else:
        if stack[-1] != S[i]:
            stack.pop()
        else:
            stack.append(S[i])

print(N - len(stack))
