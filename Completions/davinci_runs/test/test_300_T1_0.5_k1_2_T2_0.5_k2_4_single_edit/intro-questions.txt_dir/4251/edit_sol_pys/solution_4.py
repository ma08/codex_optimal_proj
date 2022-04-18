from collections import OrderedDict



def solution(matrix, n, m):
    max_diff = 0
    for j in range(m):
        column = [matrix[i][j] for i in range(n)]
        column.sort()
        for i in range(n-1):
            diff = column[i+1] - column[i]
            if diff > max_diff:
                max_diff = diff


def solution2(matrix, n, m):
    max_diff = 0
    for j in range(m):
        column = OrderedDict()
        for i in range(n):
            if matrix[i][j] not in column:
                column[matrix[i][j]] = 1
            else:
                column[matrix[i][j]] += 1
        count = 0
        for key in column:
            count += column[key]
            if key + 1 in column:
                diff = column[key + 1]
            else:
                diff = n - count
            if diff > max_diff:
                max_diff = diff
    return max_diff


    return max_diff


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution2(matrix, n, m))
