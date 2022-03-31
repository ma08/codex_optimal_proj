

n, r = map(int, input().split())

projects = []
for _ in range(n):
    projects.append(list(map(int, input().split())))

projects.sort(key=lambda x: x[0])

i = 0
j = 0
while i < n:
    if r >= projects[i][0]:
        r += projects[i][1]
        if r < 0:
            break
        i += 1
    else:
        j += 1

print(i)