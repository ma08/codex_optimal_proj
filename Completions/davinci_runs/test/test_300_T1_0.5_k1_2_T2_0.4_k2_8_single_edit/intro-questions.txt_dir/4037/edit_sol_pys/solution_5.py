

# Решение в стиле динамики

n, w = map(int, input().split())

projects = []
for i in range(n):
    c, v = map(int, input().split())
    projects.append((c, v))

dp = [0] * (w + 1)

for i in range(n):
    for j in range(w, projects[i][0] - 1, -1):
        if dp[j] < dp[j - projects[i][0]] + projects[i][1] and j - projects[i][0] >= 0:
            dp[j] = dp[j - projects[i][0]] + projects[i][1]

print(dp[w])


# Решение в стиле выбора

# n, w = map(int, input().split())

# projects = []
# for i in range(n):
#     c, v = map(int, input().split())
#     projects.append((c, v))

# projects.sort(key=lambda x: x[0])

# count = 0
# for i in range(n):
#     if projects[i][0] <= w:
#         w += projects[i][1]
#         count += 1
#     else:
#         break

# print(count)
