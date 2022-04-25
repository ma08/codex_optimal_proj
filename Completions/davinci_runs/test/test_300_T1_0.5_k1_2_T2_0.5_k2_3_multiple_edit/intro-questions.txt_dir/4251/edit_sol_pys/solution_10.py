
def solution(matrix, rows, columns):
    max_diff = 0
    for j in range(columns):
        column = [matrix[i][j] for i in range(rows)]
        column.sort()
        for i in range(rows-1):
            diff = column[i+1] - column[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff


if __name__ == '__main__':
    rows, columns = map(int, input().split())
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, rows, columns))
