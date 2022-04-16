

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
sys.setrecursionlimit(1000000)
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n

def prime_factorization(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def f(i, n, k, a, b):
    if i == n:
        return
    if b[i] == 0:
        b[i] = prime_factorization(a[i])
    for j in range(i + 1, n):
        if b[j] == 0:
            b[j] = prime_factorization(a[j])
        if len(list(set(b[i]) & set(b[j]))) == 0:
            k -= 1
    if k == 0:
        print(a[i])
        exit()
    f(i + 1, n, k, a, b)

f(0, n, k, a, b)


# In[ ]:



