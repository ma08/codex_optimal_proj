
def main():
    """
    This is the main function.
    """
    n_val = int(input())
    matrix = []
    for _ in range(n_val):
        matrix.append(list(map(int, input().split())))

    for i in range(n_val):
        matrix[i][i] = 2**31 - 1

    for i in range(n_val):
        for j in range(i + 1, n_val):
            matrix[i][j] = matrix[i][j] | matrix[i][i]

    for i in range(n_val):
        for j in range(0, i):
            matrix[i][j] = matrix[i][j] | matrix[i][i]

    for i in range(n_val):
        for j in range(n_val):
            if i != j:
                matrix[i][i] = max(matrix[i][i], matrix[i][j])

    for i in range(n_val):
        print(matrix[i][i], end=' ')

if __name__ == '__main__':
    main()
