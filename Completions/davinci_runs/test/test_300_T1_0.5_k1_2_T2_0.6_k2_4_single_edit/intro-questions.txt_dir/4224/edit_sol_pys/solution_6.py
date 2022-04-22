#!/usr/bin/python3

N = int(input())
A = [int(x) for x in input().split()]

count = 0

for i in A:
    while i % 2 == 0:
        i /= 2
        count += 1

print(count)
