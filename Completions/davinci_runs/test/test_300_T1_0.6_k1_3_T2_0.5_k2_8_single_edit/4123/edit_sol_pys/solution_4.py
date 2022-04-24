
from collections import Counter

n = int(input())
s = input()

c = Counter(s[i:i+2] for i in range(n-1))


#python
print(max(c, key=c.get))
