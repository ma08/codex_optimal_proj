#!/usr/bin/env python3

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(len(set([a, b, c])))
