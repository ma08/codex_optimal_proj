
import sys

def solution(matrix, n, m):
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
    n, m = map(int, sys.stdin.readline().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))
    print(solution(matrix, n, m))
