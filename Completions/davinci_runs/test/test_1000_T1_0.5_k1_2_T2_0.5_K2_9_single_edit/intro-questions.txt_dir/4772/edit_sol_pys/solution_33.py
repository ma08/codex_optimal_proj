


def get_word(matrix, i, j, row, col):
    """
    Function to get word
    """
    word = matrix[i][j]
    k = j+1
    while k < col and matrix[i][k] != '#':
        word += matrix[i][k]
        k += 1
    return word

def main():
    """
    Main function
    """
    row, col = map(int, input().split())
    matrix = []
    for i in range(row):
        matrix.append(input())
    words = []
    for i in range(row):
        for j in range(col):
            if matrix[i][j] != '#':
                if j < col-1 and matrix[i][j+1] != '#':
                    word = get_word(matrix, i, j, row, col)
                    words.append(word)
                if i < row-1 and matrix[i+1][j] != '#':
                    word = matrix[i][j]
                    k = i+1
                    while k < row and matrix[k][j] != '#':
                        word += matrix[k][j]
                        k += 1
                    if word not in words:
                        words.append(word)
    print(min(words))

if __name__ == "__main__":
    main()
