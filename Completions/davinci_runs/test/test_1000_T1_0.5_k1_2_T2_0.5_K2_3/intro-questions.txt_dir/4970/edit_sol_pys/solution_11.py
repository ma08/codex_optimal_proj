

from collections import Counter

n = int(input())

combinations = []

for i in range(n):
    courses = list(map(int, input().split(" ")))
    combinations.append(tuple(sorted(courses)))

c = Counter(combinations)
most_common = c.most_common(1)

print(most_common[0][1])
