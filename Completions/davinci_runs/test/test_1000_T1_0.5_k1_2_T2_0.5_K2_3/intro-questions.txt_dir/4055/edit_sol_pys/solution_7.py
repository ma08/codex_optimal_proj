
from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))[:n]
c = Counter(a)
print(c.most_common(k)[-1][1])
