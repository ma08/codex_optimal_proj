


def solution(matrix, n, m):
    max_diff = 0
    for i in range(n):
        column = [matrix[i][j] for j in range(m)]
        column.sort()
        for j in range(m-1):
            diff = column[j+1] - column[j]
            if diff > max_diff:
                max_diff = diff
    return max_diff


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, n, m))
