from collections import Counter

n = int(input())
s = input()
c = Counter(s)
print(n - sum(c.values()))
