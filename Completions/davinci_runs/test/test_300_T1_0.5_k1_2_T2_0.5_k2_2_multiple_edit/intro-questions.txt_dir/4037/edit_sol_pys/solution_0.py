
# 1st solution

n, r = map(int, input().split())

projects = []
for i in range(n):
    a, b = map(int, input().split())
    projects.append((a, b))

projects.sort(key=lambda x: x[0])

count = 0
for i in range(n):
    if projects[i][0] <= r:
        r += projects[i][1]
        count += 1
    else:
        break

print(count)

# 2nd solution
"""
# Dynamic solution

n, r = map(int, input().split())

projects = []
for i in range(n):
    a, b = map(int, input().split())
    projects.append((a, b))

projects.sort(key=lambda x: x[0])

dp = [0] * (r + 1)

for i in range(n):
    for j in range(r, projects[i][0] - 1, -1):
        if dp[j] < dp[j - projects[i][0]] + projects[i][1] and j - projects[i][0] >= 0:
            dp[j] = dp[j - projects[i][0]] + projects[i][1]

print(dp[r])
"""
