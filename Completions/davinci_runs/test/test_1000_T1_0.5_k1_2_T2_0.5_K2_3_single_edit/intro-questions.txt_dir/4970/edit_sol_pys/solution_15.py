
from collections import Counter, defaultdict

n = int(input())
course_combinations = defaultdict(int)

for i in range(n):
    courses = list(map(int, input().split(" ")))
    course_combinations[tuple(sorted(courses))] += 1


# print(course_combinations)

most_common = Counter(course_combinations).most_common(1)
# c = Counter(course_combinations)
# most_common = c.most_common(1)

# print(most_common)

print(most_common[0][0])
