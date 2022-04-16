

n, m = map(int, raw_input().split())
d = []
for i in range(n):
    d.append(raw_input())

t = 0
for i in range(m):
    if d[0][i] == '_':
        t += 1
print(t)
