

from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

a.sort()
groups = []

for i in range(n):
    if i == 0 or a[i] != a[i-1]:
        groups.append([a[i]])
    else:
        groups[-1].append(a[i])

print(len(groups))