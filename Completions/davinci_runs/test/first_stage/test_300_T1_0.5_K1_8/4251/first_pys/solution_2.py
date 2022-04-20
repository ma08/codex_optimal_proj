

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: x[0])

for i in range(1, m):
    a.sort(key=lambda x: x[i])

diffs = []
for row in a:
    for i in range(1, m):
        diffs.append(abs(row[i] - row[i-1]))

print(max(diffs))