

def count_spaces(matrix):
    spaces = [0, 0, 0, 0, 0]
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == '#':
                continue
            elif matrix[i][j] == 'X':
                if matrix[i + 1][j] == 'X':
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            spaces[4] += 1
                        else:
                            spaces[3] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            spaces[3] += 1
                        else:
                            spaces[2] += 1
                else:
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            spaces[3] += 1
                        else:
                            spaces[2] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            spaces[2] += 1
                        else:
                            spaces[1] += 1
            else:
                if matrix[i + 1][j] == 'X':
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            spaces[3] += 1
                        else:
                            spaces[2] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            spaces[2] += 1
                        else:
                            spaces[1] += 1
                else:
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            spaces[2] += 1
                        else:
                            spaces[1] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            spaces[1] += 1
                        else:
                            spaces[0] += 1

    return spaces

def main():
    rows, columns = [int(x) for x in input().split()]
    matrix = []
    for i in range(rows):
        matrix.append(list(input()))
    spaces = count_spaces(matrix)
    for i in range(len(spaces)):
        print(spaces[i])

if __name__ == '__main__':
    main()
