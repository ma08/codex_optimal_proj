

n = int(input())
a = list(map(int, input().split())

d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = []
    d[a[i]].append(i)

c = [0] * n
for i in range(1, len(d) + 1):
    c[d[i][0]] = i

print(*c)
