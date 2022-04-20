

# SOLUTION
def min_moves(matrix):
    n, m = len(matrix), len(matrix[0])
    moves = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != i * m + j + 1:
                moves += 1
                for k in range(n):
                    if matrix[k][j] == i * m + j + 1:
                        matrix[k][j] = matrix[i][j]
                        break
    return moves

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
print(min_moves(matrix))