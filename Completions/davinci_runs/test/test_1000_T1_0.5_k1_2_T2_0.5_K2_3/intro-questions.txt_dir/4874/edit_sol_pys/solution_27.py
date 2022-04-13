n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(input())

total = 0
for i in range(m):
    if d[0][i] == '_':
        total += 1
print(total)
