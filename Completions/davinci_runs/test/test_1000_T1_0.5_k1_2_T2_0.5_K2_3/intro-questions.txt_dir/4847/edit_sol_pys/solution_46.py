
n = int(input('n = '))
m = int(input('m = '))
a = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = int(input())
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
