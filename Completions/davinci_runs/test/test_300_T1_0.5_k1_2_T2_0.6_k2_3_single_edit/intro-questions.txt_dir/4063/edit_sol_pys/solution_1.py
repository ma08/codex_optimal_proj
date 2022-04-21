#!/usr/bin/env python
# coding: utf-8


# In[ ]:


N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

cnt = 1
for i in range(N - 1):
    if A[i] == A[i + 1]:
        cnt += 1
        i += 1
print(cnt)
