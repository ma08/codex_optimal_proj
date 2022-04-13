#!/usr/bin/env python3

n, h, v = map(int, input().split())

def volume(n, h, v, n1, h1, v1):
    return 2 * (n1 - h1) * (n1 - v1) * h1 * v1

print(max(volume(n, h, v), volume(n, n - h, v), volume(n, h, n - v), volume(n, n - h, n - v)))
