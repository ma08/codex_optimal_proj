

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

c = []

for i in a:
    for j in b:
        c.append(i + j)

c.sort()

for i in range(m):
    print(c[i], end=' ')
