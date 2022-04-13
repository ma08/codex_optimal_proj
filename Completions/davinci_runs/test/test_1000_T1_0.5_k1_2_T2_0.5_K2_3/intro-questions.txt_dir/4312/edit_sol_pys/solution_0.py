
# -*- coding: utf-8 -*-

a,b,c,d = map(int, input().split())

if (a <= c and b < d) or (a < c and b <= d):
    print("No")
else:
    print("Yes")
