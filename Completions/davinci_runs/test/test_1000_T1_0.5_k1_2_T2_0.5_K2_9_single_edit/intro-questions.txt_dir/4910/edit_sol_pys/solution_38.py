

from collections import defaultdict

n = int(input())  # number of students
costumes = [input() for _ in range(n)]  # costumes of students

counts = defaultdict(int)  # counts of costumes
for costume in costumes:
    counts[costume] += 1

max_count = max(counts.values())  # most popular costume
best_costumes = [costume for costume, count in counts.items() if count == max_count]
best_costumes.sort()  # sort alphabetically

for costume in best_costumes:
    print(costume)
