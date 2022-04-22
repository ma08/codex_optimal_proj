

n, m = map(int, input().split())
a = list(map(int, input().split()) for i in range(n))

x1 = 0
x2 = 0
y1 = 0
y2 = 0

for i in range(n): 
    for j in range(m):
        if i == j:
            x1 += a[i][j]
        if i + j == n - 1:
            x2 += a[i][j]
        if i == 0 or i == n - 1:
            y1 += a[i][j]
        if j == 0 or j == m - 1:
            y2 += a[i][j]

print(max(x1, x2, y1, y2))
