

def solution(matrix, n, m, k):
    max_diff = 0
    for i in range(n):
        for j in range(m):
            for x in range(n):
                for y in range(m):
                    if i == x and j == y:
                        continue
                    if matrix[i][j] - matrix[x][y] > max_diff:
                        max_diff = matrix[i][j] - matrix[x][y]
    return max_diff - k


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    k = int(input())
    print(solution(matrix, n, m, k))
