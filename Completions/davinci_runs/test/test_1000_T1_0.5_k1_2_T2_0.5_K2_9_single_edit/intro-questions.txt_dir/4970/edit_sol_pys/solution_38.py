from collections import defaultdict


frosh = int(input())
classes = defaultdict(lambda: 0)
for _ in range(frosh):
    courses = tuple(sorted(map(int, input().split())))
    classes[courses] += 1
print(max(classes.values()))
