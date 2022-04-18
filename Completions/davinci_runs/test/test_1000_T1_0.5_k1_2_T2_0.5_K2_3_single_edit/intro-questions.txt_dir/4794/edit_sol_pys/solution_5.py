
def count_parking_spaces(matrix):
    parking_spaces = [0, 0, 0, 0, 0]
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == '#':
                continue
            elif matrix[i][j] == 'X':
                if matrix[i + 1][j] == 'X':
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            parking_spaces[4] += 1
                        else:
                            parking_spaces[3] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            parking_spaces[3] += 1
                        else:
                            parking_spaces[2] += 1
                else:
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            parking_spaces[3] += 1
                        else:
                            parking_spaces[2] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            parking_spaces[2] += 1
                        else:
                            parking_spaces[1] += 1
            else:
                if matrix[i + 1][j] == 'X':
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            parking_spaces[3] += 1
                        else:
                            parking_spaces[2] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            parking_spaces[2] += 1
                        else:
                            parking_spaces[1] += 1
                else:
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            parking_spaces[2] += 1
                        else:
                            parking_spaces[1] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            parking_spaces[1] += 1
                        else:
                            parking_spaces[0] += 1

    return parking_spaces

def main():
    rows, columns = [int(x) for x in input().split()]
    matrix = []
    for i in range(rows):
        matrix.append(list(input()))
    parking_spaces = count_parking_spaces(matrix)
    for i in range(len(parking_spaces)):
        print(parking_spaces[i])

if __name__ == '__main__':
    main()
