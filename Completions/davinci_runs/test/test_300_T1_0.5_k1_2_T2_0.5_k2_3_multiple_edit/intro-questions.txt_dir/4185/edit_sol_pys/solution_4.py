def get_min_moves(matrix):
    n = len(matrix)  # num rows
    m = len(matrix[0])  # num cols

    moves = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != (i * m) + j + 1:  # if not in place
                moves += 1
    return moves


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    print(get_min_moves(matrix))
