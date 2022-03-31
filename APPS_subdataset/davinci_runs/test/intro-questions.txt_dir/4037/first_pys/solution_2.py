

#Program

n, r = map(int, input().split())
projects = []
for _ in range(n):
    projects.append(list(map(int, input().split())))

projects = sorted(projects, key=lambda x: x[0])

count = 0
for a, b in projects:
    if a > r:
        break
    r += b
    count += 1

print(count)