

raw_input()
r = int(raw_input())

projects = []
for i in range(int(raw_input())):
    projects.append(map(int, raw_input().split()))

projects.sort(key=lambda x: x[1])

ans = 0
for x in projects:
    if r >= x[0]:
        ans += 1
        r += x[1]

print ans