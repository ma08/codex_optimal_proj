#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math


# In[ ]:


def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


# In[ ]:


def main():
    N = int(input())
    res = 0
    for i in range(1, N+1):
        if is_prime(i):
            res += 1
    print(res)


# In[ ]:


if __name__ == "__main__":
    main()


# In[ ]:






N = int(input())

odd = 0
for i in range(1, N+1):
    if i % 2 != 0:
        odd += 1

print(odd/N)
