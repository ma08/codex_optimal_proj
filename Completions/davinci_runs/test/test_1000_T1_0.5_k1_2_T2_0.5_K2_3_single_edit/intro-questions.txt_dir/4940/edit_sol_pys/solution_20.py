
n, m = map(int, input().split())

p = []
for i in range(n):
    p.append(list(map(int, input().split())))

t = [0] * n

for j in range(m):
    for i in range(n):
        if j == 0:
            t[i] = p[i][j]
        else:
            t[i] += p[i][j]
        for k in range(n):
            if k != i and t[k] + p[k][j] >= t[i]:
                t[k] = t[i] - p[k][j] - 1

print(" ".join(map(str, t)))
