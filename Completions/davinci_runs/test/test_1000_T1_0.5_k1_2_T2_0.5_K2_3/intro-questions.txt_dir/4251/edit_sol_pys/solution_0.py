
def solution(matrix, n, m, k):
    for i in range(n):
        row = matrix[i]
        row.sort()
        for j in range(m-1):
            diff = row[j+1] - row[j]
            if diff > max_diff:
                max_diff = diff
    max_diff = 0
    for j in range(m):
        column = [matrix[i][j] for i in range(n)]
        column.sort()
        for i in range(n-1):
            diff = column[i+1] - column[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, n, m, k))
