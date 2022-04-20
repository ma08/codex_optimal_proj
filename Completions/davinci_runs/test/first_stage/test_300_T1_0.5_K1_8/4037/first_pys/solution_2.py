

n, r = map(int, input().split())

projects = []

for _ in range(n):
    a, b = map(int, input().split())
    projects.append([a, b])

projects.sort()

for i in range(n):
    projects[i][0] = projects[i][0] - r
    if i > 0:
        projects[i][0] = projects[i][0] + projects[i-1][1]

projects.sort()

ans = 0

for i in range(n):
    if projects[i][0] > 0:
        break
    ans += 1

print(ans)