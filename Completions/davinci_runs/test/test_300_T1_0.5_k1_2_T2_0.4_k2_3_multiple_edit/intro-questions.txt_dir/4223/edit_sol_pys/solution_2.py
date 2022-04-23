import collections

n = int(input())
s = list(input())

c = collections.Counter(s)

c = Counter(s)

ans = n - sum(c.values())

print(ans)
