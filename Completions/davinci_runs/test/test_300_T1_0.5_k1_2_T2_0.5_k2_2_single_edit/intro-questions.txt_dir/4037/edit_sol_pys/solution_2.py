

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
