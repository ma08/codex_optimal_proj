
def count_parking_space(matrix):
    parking_space = [0, 0, 0, 0, 0, 0, 0]
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == '#':
                continue
            elif matrix[i][j] == 'X' and matrix[i + 1][j] == 'X' and matrix[i][j + 1] == 'X' and matrix[i + 1][j + 1] == 'X':
                parking_space[6] += 1
            elif matrix[i][j] == 'X' and matrix[i + 1][j] == 'X':
                parking_space[5] += 1
            elif matrix[i][j] == 'X' and matrix[i][j + 1] == 'X':
                parking_space[5] += 1
            elif matrix[i][j] == 'X':
                if matrix[i + 1][j] == 'X':
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            parking_space[4] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            parking_space[3] += 1
                else:
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            parking_space[3] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            parking_space[2] += 1
            else:
                if matrix[i + 1][j] == 'X':
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            parking_space[3] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            parking_space[2] += 1
                else:
                    if matrix[i][j + 1] == 'X':
                        if matrix[i + 1][j + 1] == 'X':
                            parking_space[2] += 1
                    else:
                        if matrix[i + 1][j + 1] == 'X':
                            parking_space[1] += 1

    return parking_space[::-1]

def main():
    rows, columns = [int(x) for x in input().split()]
    matrix = []
    for i in range(rows):
        matrix.append(list(input()))
    parking_space = count_parking_space(matrix)
    for i in range(len(parking_space)):
        print(parking_space[i])

if __name__ == '__main__':
    main()
