#!/usr/bin/env python
# coding: utf-8
# In[ ]:

n = int(input())
b = list(map(int, input().split()))

a = []

for i in range(n-1):
    if b[i] <= b[i+1]:
        a.append(b[i])
    else:
        a.append(b[i+1])

a.append(b[n-2])


# In[ ]:



print(sum(a))
