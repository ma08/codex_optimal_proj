

# Решение в стиле динамики

n, m = map(int, input().split())

projects = []
for i in range(m):
    a, b, c = map(int, input().split())
    projects.append((a, b, c))

projects.sort(key=lambda x: x[0])

dp = [0] * (n + 1)

for i in range(m):
    for j in range(projects[i][2]):
        for k in range(n, projects[i][0] - 1, -1):
            if dp[k] < dp[k - projects[i][0]] + projects[i][1]:
                dp[k] = dp[k - projects[i][0]] + projects[i][1]

print(dp[n])
