

from collections import Counter

n = int(input())
v = list(map(int, input().split()))

c = Counter(v)

if len(c.keys()) == 1:
    print(0)
elif len(c.keys()) == 2:
    print(n - max(c.values()) * 2)
else:
    print(-1)