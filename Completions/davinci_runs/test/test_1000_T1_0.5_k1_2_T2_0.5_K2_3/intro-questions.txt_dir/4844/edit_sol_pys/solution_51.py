

def main():
    """
    This is the main function.
    """
    n_val = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n_val)]

    for i in range(n_val):
        matrix[i][i] = 2**31 - 1

    print(matrix)

if __name__ == '__main__':
    main()
