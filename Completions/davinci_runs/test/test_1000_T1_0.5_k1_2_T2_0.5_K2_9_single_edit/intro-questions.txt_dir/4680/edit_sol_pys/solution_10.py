# coding=utf-8

import sys

a, b, c = map(int, sys.stdin.readline().split())

if a + b == c or a + c == b or b + c == a:
    print("YES")
else:
    print("NO")
