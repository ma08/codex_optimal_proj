"""
This program is for counting the votes for a particular candidate
"""

from collections import Counter

NUM_OF_VOTES = int(input())
VOTES = [input() for _ in range(NUM_OF_VOTES)]
c = Counter(votes)

MAX_COUNT = max(c.values())

print("\n".join(sorted([v for v in c.keys() if c[v] == MAX_COUNT])))
