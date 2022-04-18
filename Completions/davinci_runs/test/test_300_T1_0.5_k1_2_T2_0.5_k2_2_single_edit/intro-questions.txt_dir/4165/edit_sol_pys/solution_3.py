
# coding: utf-8

# In[1]:



N = int(input())
L = list(map(int, input().split()))

# In[2]:


L.sort()

# In[3]:


if L[0] + L[1] > L[-1]:


# In[4]:

    print("Yes")
else:
    print("No")
