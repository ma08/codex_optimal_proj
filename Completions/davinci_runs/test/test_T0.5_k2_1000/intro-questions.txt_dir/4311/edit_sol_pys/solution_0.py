#!/usr/bin/env python3

import sys

def f(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1
s=int(input())
a=[]
a.append(s)
for i in range(1,1000000):
    a.append(f(a[i-1]))
    if a[i]==a[i-1]:
        print(i)
        sys.exit()
