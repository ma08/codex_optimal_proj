
from collections import Counter
n = int(input())
c = Counter([input().split()[1] for _ in range(n)])
print(c['soft'] * c['hard'])
