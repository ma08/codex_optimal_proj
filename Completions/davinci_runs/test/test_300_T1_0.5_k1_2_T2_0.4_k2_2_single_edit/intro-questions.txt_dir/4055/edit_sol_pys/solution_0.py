

n, m = map(int, input().split())
a = list(map(int, input().split()))  # n
b = list(map(int, input().split()))  # m
c = []

for i in range(m):
    c.append(b[i])

for i in range(n):
    c.append(a[i])

print(c)
