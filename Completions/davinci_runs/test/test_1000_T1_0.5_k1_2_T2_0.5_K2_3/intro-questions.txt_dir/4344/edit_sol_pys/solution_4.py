
# coding: utf-8

# In[1]:


n, k = map(int, input().split())
a = list(map(int, input().split()))

if len(set(a)) < k:
    print('NO')
else:
    b = []
    print('YES')
    for i in range(n):
        if k > 0:
            if a[i] not in a[:i]:
                b.append(i+1)
    for i in b:
        print(i, end=' ')
                k -= 1
