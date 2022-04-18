
'''
from collections import Counter

num_of_votes = int(input())
votes = [input() for _ in range(num_of_votes)]

c = Counter(votes)

max_count = max(c.values())

'''
print("\n".join(sorted([v for v in c.keys() if c[v] == max_count])))
