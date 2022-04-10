

n, r = map(int, input().split())

projects = []
for i in range(n):
    projects.append(list(map(int, input().split())))

def solve(n, r, projects):
    projects.sort(key=lambda x: x[1])
    for i in range(n):
        r += projects[i][1]
        if r < projects[i][0]:
            return "NO"
    return "YES"

print(solve(n, r, projects))