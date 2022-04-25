
def solution(matrix, row_num, col_num):
    max_diff = -1000000000
    for j in range(col_num):
        col = [matrix[i][j] for i in range(row_num)]
        col.sort()
        for i in range(row_num - 1):
            diff = col[i + 1] - col[i]
            if diff > max_diff:
                max_diff = diff
    return max_diff if max_diff > 0 else -1


if __name__ == '__main__':
    row_num, col_num = map(int, input().split())
    matrix = []
    for _ in range(row_num):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, row_num, col_num))
