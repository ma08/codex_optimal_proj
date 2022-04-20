
def solution(matrix):
    n = len(matrix)
    m = len(matrix[0])
    k = -1
    for i in range(m):
        col = [matrix[j][i] for j in range(n)]
        col.sort()
        for j in range(n - 1):
            k = max(k, col[j + 1] - col[j])
    return k

if __name__ == "__main__":
    n, m = [int(s) for s in input().split(" ")]
    matrix = []
    for i in range(n):
        matrix.append([int(s) for s in input().split(" ")])
    print(solution(matrix))
