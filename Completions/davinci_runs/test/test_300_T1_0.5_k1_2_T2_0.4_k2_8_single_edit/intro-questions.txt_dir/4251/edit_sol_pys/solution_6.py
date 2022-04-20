

def solution(matrix, n, m):
    max_diff = 0
    for i in range(n-1):
        row = matrix[i]
        row.sort()
        for j in range(m-1):
            diff = row[j+1] - row[j]
            max_diff = max(max_diff, diff)
    return max_diff


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, n, m))
