#!/usr/bin/env python3


n = int(input())
recited = []

for i in range(n):
    recited.append(int(input()))

for i in range(1, recited[-1] + 1):
    if i not in recited:
        print(i)

if len(recited) == recited[-1]:
    print("Good job")
