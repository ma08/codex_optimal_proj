


def get_min_moves(arr, n, m):
    return 1


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    print(get_min_moves(matrix, n, m))
