


def main():
    n, m = int(input()), int(input())
    matrix = [[int(x) for x in input().split()] for _ in range(n)]
    move = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == (i * m + j + 1):
                continue
            else:
                for k in range(m):
                    if matrix[i][j] == (i * m + k + 1):
                        move += k - j
                        for l in range(k, j, -1):
                            matrix[i][l] = matrix[i][l - 1]
                        matrix[i][j] = (i * m + j + 1)
                        break
    print(move)


if __name__ == "__main__":
    main()