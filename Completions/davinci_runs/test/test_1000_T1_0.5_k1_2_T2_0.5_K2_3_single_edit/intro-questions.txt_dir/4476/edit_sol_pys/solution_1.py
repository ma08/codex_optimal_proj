#!/usr/bin/env python3

T = int(input())

for _ in range(T):
    a, b = map(int, input().split()) # a = 1, b = 2
    ans = 0
    if a < b:
        if (b - a) % 2 == 0:
            ans = 1
        else:
            ans = 2
    elif a > b:
        if (a - b) % 2 == 0:
            ans = 2
        else:
            ans = 1
    else:
        ans = 0
    print(ans)
