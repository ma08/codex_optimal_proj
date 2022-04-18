"""
Given a N x M matrix, find the number of moves required to sort the matrix in ascending order. A move consists of choosing any element and placing it at the end of the row.
"""


def get_min_moves(matrix):
    n = len(matrix)
    m = len(matrix[0])

    moves = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != (i * m) + j + 1:
                moves += 1
    return moves


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    print(get_min_moves(matrix))
