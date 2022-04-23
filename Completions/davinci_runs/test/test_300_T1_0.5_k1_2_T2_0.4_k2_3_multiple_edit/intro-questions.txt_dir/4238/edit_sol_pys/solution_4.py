#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = input().rstrip()

if N.isdigit():
    if sum(map(int, N)) % 9 == 0:
        print("Yes")
    else:
        print("No")
