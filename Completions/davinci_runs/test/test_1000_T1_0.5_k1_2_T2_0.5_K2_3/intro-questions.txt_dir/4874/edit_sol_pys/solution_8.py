n, m = map(int, input().split())
d = [input() for i in range(n)]

t = 0
for i in range(n):
    if d[0][i] == '_':
        t += 1

print(t)
