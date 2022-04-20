

n, r = map(int, input().split())
projects = []

for i in range(n):
    projects.append(list(map(int, input().split())))

def canComplete(r, projects):
    for project in projects:
        if project[0] > r:
            return False
        r += project[1]
        if r < 0:
            return False
    return True

print("YES" if canComplete(r, projects) else "NO")