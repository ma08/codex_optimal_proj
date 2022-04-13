

#%%
from collections import Counter

n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

ans = 0
for i in c:
    if c[i] > i:
        ans += c[i] - i
    elif c[i] < i:
        ans += c[i]

print(ans)

#%%
n = int(input())
a = list(map(int, input().split()))

c = Counter(a)

ans = 0
for i in c:
    if c[i] > i:
        ans += c[i] - i
    elif c[i] < i:
        ans += c[i]

print(ans)
