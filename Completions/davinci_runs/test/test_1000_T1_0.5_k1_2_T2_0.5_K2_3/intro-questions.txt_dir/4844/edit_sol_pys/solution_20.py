

def main():
    """
    This is the main function.
    """
    n_val = int(input())
    matrix = []
    for _ in range(n_val):
        matrix.append(list(map(int, input().split())))

    for i in range(n_val):  # diagonal elements
        matrix[i][i] = 2**31 - 1  # 2^31 - 1

    print(matrix)  # just to check

if __name__ == '__main__':
    main()
