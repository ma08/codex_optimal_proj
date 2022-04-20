

from typing import List

def sort_binary_matrix(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    row_inverted = [False] * n
    col_inverted = [False] * m
    for i in range(n):
        for j in range(1, m):
            if matrix[i][j] < matrix[i][j - 1]:
                row_inverted[i] = not row_inverted[i]
                break
    for j in range(m):
        for i in range(1, n):
            if matrix[i][j] < matrix[i - 1][j]:
                col_inverted[j] = not col_inverted[j]
                break
    for i in range(n):
        for j in range(1, m):
            if matrix[i][j] < matrix[i][j - 1]:
                return False
    return True

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

if sort_binary_matrix(matrix):
    print("YES")
    print("".join(map(lambda x: "1" if x else "0", row_inverted)))
    print("".join(map(lambda x: "1" if x else "0", col_inverted)))
else:
    print("NO")