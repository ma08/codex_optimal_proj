

from collections import Counter

n = int(input())
s = input()

c = Counter(s[i:i+1] for i in range(n))

print(max(c, key=c.get))
