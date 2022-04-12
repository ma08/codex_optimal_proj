# this is a test file
from collections import defaultdict

n = int(input())
costumes = [input() for _ in range(n)]

counts = defaultdict(int)
for costume in costumes:
    counts[costume] += 1

max_count = max(counts.values())
best_costumes = [costume for costume, count in counts.items() if count == max_count]
best_costumes.sort()

for costume in best_costumes:
    print(costume)
