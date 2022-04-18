#!/usr/bin/env python3

#-----main-----
n, r = input().split()
n, r = int(n), int(r)

for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    if r < a:
        print("NO")
        exit()
    r += b

print("YES")
