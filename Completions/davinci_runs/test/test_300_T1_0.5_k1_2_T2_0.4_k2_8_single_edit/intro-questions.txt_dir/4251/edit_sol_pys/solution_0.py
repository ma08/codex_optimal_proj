import sys
sys.setrecursionlimit(10**6)



    if n == 1 and m == 1:
        return 0
def solution(matrix, n, m):
    max_diff = 0
    for i in range(n):
        for j in range(m):
            for k in range(i+1, n):
                for l in range(j+1, m):
                    diff = abs(matrix[k][l] - matrix[i][j])
                    if diff > max_diff:
                        max_diff = diff
    return max_diff


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    print(solution(matrix, n, m))
