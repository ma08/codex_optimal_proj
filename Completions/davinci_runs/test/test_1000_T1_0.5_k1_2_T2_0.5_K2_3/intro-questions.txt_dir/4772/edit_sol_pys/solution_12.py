

def main():
    """
    Main function
    """
    rows, cols = map(int, input().split())
    matrix = []
    for i in range(rows):
        matrix.append(input())
    # print(matrix)
    words = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != '#':
                if j < cols - 1 and matrix[i][j+1] != '#':
                    word = matrix[i][j]
                    k = j + 1
                    while k < cols and matrix[i][k] != '#':
                        word += matrix[i][k]
                        k += 1
                    words.append(word)
                if i < rows - 1 and matrix[i+1][j] != '#':
                    word = matrix[i][j]
                    k = i + 1
                    while k < rows and matrix[k][j] != '#':
                        word += matrix[k][j]
                        k += 1
                    words.append(word)
    print(min(words))

if __name__ == "__main__":
    main()
