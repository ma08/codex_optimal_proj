

import sys

n, m = [int(x) for x in sys.stdin.readline().split()]

matrix = []

for i in range(n):
    matrix.append([int(x) for x in sys.stdin.readline().split()])

row_inverted = [False for i in range(n)]
col_inverted = [False for i in range(m)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            row_inverted[i] = not row_inverted[i]
            col_inverted[j] = not col_inverted[j]

for i in range(n):
    for j in range(m):
        if row_inverted[i] and col_inverted[j]:
            matrix[i][j] = 1
        elif row_inverted[i] or col_inverted[j]:
            matrix[i][j] = 0

sorted_matrix = sorted([matrix[i][j] for i in range(n) for j in range(m)])

for i in range(n):
    for j in range(m):
        if matrix[i][j] != sorted_matrix[i * m + j]:
            print("NO")
            sys.exit(0)

print("YES")
print("".join([str(int(x)) for x in row_inverted]))
print("".join([str(int(x)) for x in col_inverted]))