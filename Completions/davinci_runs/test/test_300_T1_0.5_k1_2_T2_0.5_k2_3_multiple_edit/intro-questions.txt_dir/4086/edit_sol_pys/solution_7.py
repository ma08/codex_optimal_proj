#!/usr/bin/env python3

n = int(input())
a = [int(x) for x in input().split()]

def remove_duplicate(a):
    b = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            b.append(a[i])
    return b

b = remove_duplicate(a)
print(len(b))
print(*b)
