
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:20:07 2020
@author: karanwaghela
"""
# SOLUTION

n = int(input())
x = list(map(int,input().split()))
x.sort()
ans = 0
for i in range(1,n):
    ans += abs(x[i]-x[i-1])-1
print(ans)
