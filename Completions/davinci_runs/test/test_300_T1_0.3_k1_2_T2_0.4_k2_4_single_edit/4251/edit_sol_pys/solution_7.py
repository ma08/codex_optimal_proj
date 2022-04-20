

def solution(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    ans = 0
    for i in range(m):
        col = sorted([matrix[j][i] for j in range(n)])
        for j in range(n - 1):
            ans = max(ans, col[j + 1] - col[j] - k)
    return ans

if __name__ == "__main__":
    n, m = [int(s) for s in input().split(" ")]
    matrix = []
    for i in range(n):
        matrix.append([int(s) for s in input().split(" ")])
    print(solution(matrix))
