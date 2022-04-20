
def solution(matrix):
    n = len(matrix)  # number of rows
    m = len(matrix[0])  # number of columns
    k = 0  # max difference
    for i in range(m):  # iterate through columns
        col = [matrix[j][i] for j in range(n)]  # get column
        col.sort()  # sort column
        for j in range(1, n):  # iterate through sorted column
            k = max(k, col[j] - col[j - 1])  # get max difference
    return k  # return max difference

if __name__ == "__main__":
    n, m = [int(s) for s in input().split(" ")]
    matrix = []
    for i in range(n):
        matrix.append([int(s) for s in input().split(" ")])
    print(solution(matrix))
