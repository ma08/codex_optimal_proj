

def solution(matrix, n, m, t):
    max_row = None
    max_diff = 0
    for j in range(m):
        column = [matrix[i][j] for i in range(n)]
        column = sorted(column, reverse=True)
        for i in range(n):
            if (i+1) % t == 0:
                diff = column[i] - column[i+1]
            else:
                continue
            if diff > max_diff:
                max_diff = diff
    return max_diff


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, n, m))
