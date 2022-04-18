

n, m = map(int, input().split())
a = list(map(int, input().split())) + [0]
b = list(map(int, input().split())) + [0]

c = [0] * (n + m + 1)
for i in range(n + 1):
    for j in range(m + 1):
        c[i + j] += a[i] * b[j]

for i in range(n + m + 1):
    for j in range(c[i]):
        print(i, end=" ")
