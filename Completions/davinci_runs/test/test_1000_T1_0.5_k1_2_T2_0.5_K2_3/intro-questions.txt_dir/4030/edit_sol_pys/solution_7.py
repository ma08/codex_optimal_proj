import itertools

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

c = 0

for i in itertools.product([0, 1], repeat=n):
    b = [0] * m
    for j in range(n):
        if i[j] == 0:
            continue
        for k in range(m):
            b[k] += a[j][k]
    if all(x >= 1 for x in b):
        c += 1
print(c)
