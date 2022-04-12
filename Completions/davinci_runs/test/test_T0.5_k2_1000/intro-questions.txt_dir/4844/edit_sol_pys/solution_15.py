

def main():
    """
    This is the main function.
    """
    n_value = int(input())
    matrix = []
    for _ in range(n_value):
        matrix.append(list(map(int, input().split())))

    for i in range(n_value):
        matrix[i][i] = 2**31 - 1

    for i in range(n_value - 1, 0, -1):
        for j in range(i - 1, 0, -1):
            matrix[i][j] = matrix[j][i] | matrix[i][i]

    for i in range(n_value):
        for j in range(i + 1, n_value):
            matrix[i][j] = matrix[j][i] | matrix[i][i]

    for i in range(n_value):
        for j in range(n_value):
            if i != j:
                matrix[i][i] = max(matrix[i][i], matrix[i][j])

    for i in range(n_value):
        print(matrix[i][i], end=' ')

if __name__ == '__main__':
    main()
