
from sys import stdin

n = int(stdin.readline())
a = [int(x) for x in stdin.readline().split()]
d = {}
for i in range(n):
    if a[i] in d:
        d[a[i]].append(i)
    else:
        d[a[i]] = [i]
ans = n
for x in d:
    if len(d[x]) > 1:
        for i in range(len(d[x]) - 1):
            if d[x][i + 1] - d[x][i] < ans:
                ans = d[x][i + 1] - d[x][i]
for x in d:
    if len(d[x]) > 1:
        for i in range(len(d[x]) - 1):
            if d[x][i + 1] - d[x][i] == ans:
                print(d[x][i] + 1, d[x][i + 1] + 1)
                exit(0)
for x in d:
    if len(d[x]) > 1:
        for i in range(len(d[x]) - 1):
            if d[x][i + 1] - d[x][i] == ans + 1:
                print(d[x][i] + 1, d[x][i + 1] + 1)
                exit(0)
for x in d:
    if len(d[x]) > 1:
        for i in range(len(d[x]) - 1):
            if d[x][i + 1] - d[x][i] == ans + 2:
                print(d[x][i] + 1, d[x][i + 1] + 1)
                exit(0)
for x in d:
    if len(d[x]) > 1:
        for i in range(len(d[x]) - 1):
            if d[x][i + 1] - d[x][i] == ans + 3:
                print(d[x][i] + 1, d[x][i + 1] + 1)
                exit(0)
