#!/usr/bin/env python
# coding: utf-8

# In[1]:

cnt = 1
dist = 0
for i in range(N):
    dist += L[i]
    if dist <= X:
        cnt += 1
    else:
        break
print(cnt)
