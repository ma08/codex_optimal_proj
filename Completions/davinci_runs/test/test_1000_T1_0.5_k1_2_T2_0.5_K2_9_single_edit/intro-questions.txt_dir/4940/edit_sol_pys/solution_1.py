
n, m = map(int, input().split())

p = []
for i in range(n):
    p.append(list(map(int, input().split())))  # p[i][j]

t = [0] * n  # t[i]

for j in range(m):
    for i in range(n):
        if j == 0:
            t[i] = p[i][j]
        else:
            t[i] += p[i][j]
        for k in range(n):  # k != i
            if t[k] + p[k][j] > t[i]:
                t[k] = t[i] - p[k][j]  # t[i] - p[k][j]

print(" ".join(map(str, t)))
