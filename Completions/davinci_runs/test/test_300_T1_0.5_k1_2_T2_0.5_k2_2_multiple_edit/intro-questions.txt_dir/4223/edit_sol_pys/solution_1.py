

# ABC035 C

from collections import Counter

n = int(input())
s = input()

c = Counter(s)

ans = n - max(c.values())

print(ans)
