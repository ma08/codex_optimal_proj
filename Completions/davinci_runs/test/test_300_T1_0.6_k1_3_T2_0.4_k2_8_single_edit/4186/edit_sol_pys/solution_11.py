

from collections import Counter

n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
print(sum((c[i] - 2) * i for i in c if c[i] > 1)) 
