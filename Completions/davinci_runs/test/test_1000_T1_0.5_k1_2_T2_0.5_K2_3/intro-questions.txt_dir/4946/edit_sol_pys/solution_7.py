
from collections import Counter
# TODO: solve this problem

n = int(input())
languages = [int(x) for x in input().split()]


# for i in range(len(languages)):
#     for j in range(i + 1, len(languages)):
#         if languages[i] == languages[j]:
#             # find the distance between i and j
#             distance = abs(i - j)
#             print(distance)

print(Counter(languages))
