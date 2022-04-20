


def get_min_moves(arr):
    n = len(arr)
    m = len(arr[0])

    moves = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != (i * m) + j + 1:
                moves += 1
    return moves


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    print(get_min_moves(arr))
