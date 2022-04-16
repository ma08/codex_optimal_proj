

from collections import Counter

n = int(input())
votes = [input() for _ in range(n)]

c = Counter(votes)

max_count = max(c.values())

print("\n".join(sorted([v for v in c.keys() if c[v] == max_count])))
