
def solution(matrix, n, m):
    max_diff = 0
    for i in range(n):
        row = [matrix[i][j] for j in range(m)]
        row.sort()
        for j in range(m-1):
            diff = row[j+1] - row[j]
            if diff > max_diff: max_diff = diff
    return max_diff


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, n, m))
