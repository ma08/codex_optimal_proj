

def main():
    """
    This is the main function.
    """
    n_val = int(input("Enter the value of n: "))
    matrix = []
    for _ in range(n_val):
        matrix.append(list(map(int, input("Enter row: ").split())))

    for i in range(n_val):
        matrix[i][i] = 2**31 - 1

    print(matrix)

if __name__ == '__main__':
    main()
