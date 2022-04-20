
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            c[i] = 1
for i in range(n):
    if c[i] == 1:
        print(a[i], end=' ')
