#!/usr/bin/env python3

n = int(input())
a = [int(i) for i in input().split()]

def is_complete(b):
    for i in range(1, len(b)):
        if b[i] != b[i-1]:
            return False
    return True

def solve(a):
    if is_complete(a):
        return "YES"
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            b = a[:]
            b[i] += 1
            b[i+1] += 1
            if is_complete(b):
                return "YES"
    return "NO"

print(solve(a))
