
def solution(matrix, N, M):
    max_diff = 0
    for j in range(M):
        column = [matrix[i][j] for i in range(N)]
        column.sort()
        for i in range(N - 1):
            diff = column[i + 1] - column[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff


if __name__ == '__main__':
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, N, M))
