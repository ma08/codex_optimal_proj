
def solution(matrix):
    n = len(matrix)
    m = len(matrix[0])
    k = 0
    for i in range(m):
        col = [matrix[j][i] for j in range(n)]
        col.sort()
        for j in range(1, n):
            k = max(k, col[j] - col[j - 1])
    return k

if __name__ == "__main__":
    n, m = [int(s) for s in input().split(" ")]
    matrix = []
    for i in range(n):
        matrix.append([int(s) for s in input().split(" ")])
    print(solution(matrix))
