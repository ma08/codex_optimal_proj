
from collections import Counter

n, k = map(int, input().split())
a = list(map(int, input().split()))

c = Counter(a)

t = []
for i in range(k):
    t.append(c.most_common(1)[0][0])
    c[t[-1]] -= 1

print(*t)
