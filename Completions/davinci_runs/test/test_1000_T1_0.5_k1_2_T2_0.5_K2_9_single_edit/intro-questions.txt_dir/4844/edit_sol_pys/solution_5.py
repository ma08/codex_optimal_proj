

def main():
    """
    This is the main function.
    """
    n_val = int(input()) # number of nodes
    matrix = []
    for _ in range(n_val): # input the graph
        matrix.append(list(map(int, input().split())))

    for i in range(n_val): # set diagonal values to infinity
        matrix[i][i] = 2**31 - 1

    for i in range(n_val - 1, -1, -1): # update upper triangle
        for j in range(i - 1, -1, -1):
            matrix[i][j] = matrix[j][i] | matrix[i][i]

    for i in range(n_val): # update lower triangle
        for j in range(i + 1, n_val):
            matrix[i][j] = matrix[j][i] | matrix[i][i]

    for i in range(n_val): # update the diagonal
        for j in range(n_val):
            if i != j:
                matrix[i][i] = max(matrix[i][i], matrix[i][j])

    for i in range(n_val): # print the result
        print(matrix[i][i], end=' ')

if __name__ == '__main__':
    main()
