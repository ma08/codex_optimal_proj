

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

for i in range(m):
    a[0][i] = 1
for i in range(n):
    a[i][0] = 1

for i in range(1, n):
    for j in range(1, m):
        a[i][j] = a[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]

for i in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    print(a[x2 - 1][y2 - 1] - a[x2 - 1][y1 - 1] - a[x1 - 1][y2 - 1] + a[x1 - 1][y1 - 1])
