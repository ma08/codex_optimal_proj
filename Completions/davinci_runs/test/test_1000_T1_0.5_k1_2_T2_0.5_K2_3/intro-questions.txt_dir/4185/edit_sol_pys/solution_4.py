def get_min_moves(mat):
    n = len(mat)
    m = len(mat[0])

    moves = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] != (i * m) + j + 1:
                moves += 1
    return moves


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))

    print(get_min_moves(mat))
