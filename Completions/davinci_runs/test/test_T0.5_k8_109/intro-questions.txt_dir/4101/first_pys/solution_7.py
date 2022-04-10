

n, m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split())))

row_inverted = []
col_inverted = []

for i in range(n):
    row_inverted.append(0)

for i in range(m):
    col_inverted.append(0)

for i in range(n):
    for j in range(m):
        if i != 0 and i != n - 1 and j != 0 and j != m - 1:
            if matrix[i][j] == 1:
                row_inverted[i] = 1
                col_inverted[j] = 1

for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            if matrix[i][j] == 0:
                row_inverted[i] = 1
                col_inverted[j] = 1

for i in range(1, n - 1):
    if row_inverted[i] == 1:
        if matrix[i - 1][0] == 1 or matrix[i + 1][0] == 1:
            row_inverted[i - 1] = 1
            row_inverted[i + 1] = 1

for j in range(1, m - 1):
    if col_inverted[j] == 1:
        if matrix[0][j - 1] == 1 or matrix[0][j + 1] == 1:
            col_inverted[j - 1] = 1
            col_inverted[j + 1] = 1

for i in range(n):
    for j in range(m):
        if matrix[i][j] != (row_inverted[i] ^ col_inverted[j]):
            print("NO")
            exit(0)

print("YES")

for i in range(n):
    print(row_inverted[i], end='')

print()

for i in range(m):
    print(col_inverted[i], end='')