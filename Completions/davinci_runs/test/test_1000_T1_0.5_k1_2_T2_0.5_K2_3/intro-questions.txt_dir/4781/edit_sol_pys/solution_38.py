#!/usr/bin/env python3

K = int(input())
N = int(input())

for i in range(N):
    t, z = input().split(' ')
    t = int(t)
    if (t + K) % 8 == 0:
        K = 8
    else:
        K = (t + K) % 8

print(K)
