


def check(matrix, n, m):
    # print(matrix, n, m)
    if n == m:
        if n == 1:
            return True
        else:
            return matrix[0][0] == matrix[0][1] and matrix[1][0] == matrix[1][1] and matrix[0][0] == matrix[1][0]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != matrix[j][i]:
                return False

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != matrix[n - i - 1][m - j - 1] or matrix[i][j] != matrix[m - i - 1][n - j - 1]:
                return False

    return True


def main():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        matrix = []
        for j in range(n):
            matrix.append(list(map(int, input().split())))
            matrix.append(list(map(int, input().split())))

        if check(matrix, n, m):
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()