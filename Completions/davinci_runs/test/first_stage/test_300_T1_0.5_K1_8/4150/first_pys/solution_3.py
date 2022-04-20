

import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))

# a = [2, 4, 5, 3, 1]
# n = 5
# k = 2

# a = [2, 1, 3, 5, 4]
# n = 5
# k = 1

# a = [7, 2, 1, 3, 5, 4, 6]
# n = 7
# k = 1

# a = [2, 4, 5, 3, 1]
# n = 5
# k = 1

team = [0] * n

# print(a)
while len(a) > 0:
    # print(a)
    max_skill = max(a)
    max_skill_index = a.index(max_skill)
    left_k = min(max_skill_index, k)
    right_k = min(n - 1 - max_skill_index, k)
    # print(left_k, right_k)
    for i in range(max_skill_index - left_k, max_skill_index + right_k + 1):
        team[i] = 1
    for i in range(max_skill_index - left_k, max_skill_index + right_k + 1):
        a.remove(bisect.bisect_left(a, a[i]))

print("".join(map(str, team)))