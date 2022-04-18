#!/usr/bin/env python
# coding: utf-8


# In[1]:


n = int(input()) 
a = [int(i) for i in input().split()] 
a.sort() 
alice = 0 
bob = 0 
for i in range(n): 
    if i % 2 == 0: 
        alice += a[n - i - 1] 
    else: 
        bob += a[n - i - 1] 
print(alice, bob) 


# In[ ]:



