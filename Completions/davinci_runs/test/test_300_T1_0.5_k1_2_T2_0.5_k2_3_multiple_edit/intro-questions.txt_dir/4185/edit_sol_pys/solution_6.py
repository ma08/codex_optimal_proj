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


def solution(A):
    n = len(A)
    if n == 0:
        return -1
    if n == 1:
        return 0

    peaks = []
    for i in range(1, n - 1):
        if A[i - 1] < A[i] > A[i + 1]:
            peaks.append(i)

    if len(peaks) == 0:
        return 0

    for size in range(len(peaks), 0, -1):
        if n % size == 0:
            block_size = n // size
            found = [False] * size
            found_cnt = 0
            for peak in peaks:
                block_index = peak // block_size
                if found[block_index] == False:
                    found[block_index] = True
                    found_cnt += 1

            if found_cnt == size:
                return size

    return 0
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    print(get_min_moves(matrix))
