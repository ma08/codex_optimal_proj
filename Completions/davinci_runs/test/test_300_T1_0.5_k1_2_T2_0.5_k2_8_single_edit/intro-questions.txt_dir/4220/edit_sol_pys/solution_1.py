
# coding: utf-8

# In[ ]:



k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:

    print(s[:k] + "...")
