
n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(input())

t = 0
for i in range(m):
    for j in range(n):
        if d[j][i] == '_':
            t += 1
print(t)
