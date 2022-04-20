

# Solution

n, r = map(int, input().split())

projects = []
for i in range(n):
    a, b = map(int, input().split())
    projects.append((a, b))

projects.sort(key=lambda x: x[0])

# print(projects)

count = 0
for a, b in projects:
    if a <= r:
        r += b
        count += 1
    else:
        break

print(count)