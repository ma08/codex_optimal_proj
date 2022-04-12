#!/usr/bin/env python3

n = int(input())

for i in range(n):
    a, b, c, d = map(int, input().split())
    if a == b:
        print(a, c, sep=' ')
    elif c == d:
        print(a, c, sep=' ')
    elif a == c:
        print(a, b, sep=' ')
    elif b == d:
        print(a, b, sep=' ')
    elif a == d:
        print(a, c, sep=' ')
    elif b == c:
        print(a, b, sep=' ')
    else:
        print(a, c, sep=' ')
