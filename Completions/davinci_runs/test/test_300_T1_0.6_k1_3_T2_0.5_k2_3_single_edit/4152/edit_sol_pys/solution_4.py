

n = int(input())
l = list(map(int,input().split()))
from collections import Counter
c = Counter(l)
c1 = []
for i in range(len(c)):
    c1.append(c[i])
print(n-max(c.values()))
