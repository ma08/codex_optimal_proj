#!/usr/bin/env python3

a, b, c = map(int, input().split())
if b-a == c-b:
    print("YES")
else:
    print("NO")
