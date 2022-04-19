#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
s = input()

def is_regular(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

def solve(s):
    if is_regular(s):
        return 0
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == -1:
            return 1
    return 1

print(solve(s))
