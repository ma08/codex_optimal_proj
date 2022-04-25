

def solution(matrix, m, n):
    max_diff = 0
    for j in range(n):
        column = [matrix[i][j] for i in range(m)]
        column.sort()
        for i in range(m-1):
            diff = column[i+1] - column[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, n, m))
