

def main():
    """
    This is the main function.
    """
    n_val = int(input())  # number of nodes
    matrix = []
    for _ in range(n_val):  # reading the adjacency matrix
        matrix.append(list(map(int, input().split())))

    for i in range(n_val):  # setting the diagonal elements to max value
        matrix[i][i] = 2**31 - 1

    for i in range(n_val - 1, 0, -1):  # setting the upper triangular matrix
        for j in range(i - 1, 0, -1):
            matrix[i][j] = matrix[j][i] | matrix[i][i]

    for i in range(n_val):  # setting the lower triangular matrix
        for j in range(i + 1, n_val):
            matrix[i][j] = matrix[j][i] | matrix[i][i]

    for i in range(n_val):  # setting the diagonal elements to max value
        for j in range(n_val):
            if i != j:
                matrix[i][i] = max(matrix[i][i], matrix[i][j])

    for i in range(n_val):  # printing the diagonal elements
        print(matrix[i][i], end=' ')

if __name__ == '__main__':
    main()
