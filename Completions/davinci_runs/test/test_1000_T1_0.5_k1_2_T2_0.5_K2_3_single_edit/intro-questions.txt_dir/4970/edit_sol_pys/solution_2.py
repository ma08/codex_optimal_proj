

# from collections import Counter

# n = int(input())

# course_combinations = []

# for i in range(n):
#     courses = list(map(int, input().split(" ")))
#     course_combinations.append(tuple(sorted(courses)))

# # print(course_combinations)

# c = Counter(course_combinations)
# most_common = c.most_common(1)

# # print(most_common)

# print(most_common[0][1])

n = int(input())

for i in range(n):
    s = input()
    if len(s) > 10:
        print(s[0] + str(len(s) - 2) + s[-1])
    else:
        print(s)
