

from collections import Counter

n, k = map(int, input().split())
s = list(map(int, input().split()))
c = Counter(s)
t = []
for i in range(k):
    t.append(c.most_common(1)[0][0])
    c[t[-1]] -= 1

print(*t)
