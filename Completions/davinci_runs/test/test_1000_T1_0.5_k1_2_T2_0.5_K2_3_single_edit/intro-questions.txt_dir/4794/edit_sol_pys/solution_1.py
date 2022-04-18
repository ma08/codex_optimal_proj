
# CODE:

r, c = map(int, input().split())

matrix = []

for i in range(r):
    matrix.append(list(input()))

count = [0, 0, 0, 0, 0]

for i in range(r-1):
    for j in range(c-1):
        if matrix[i][j] == '.' and matrix[i][j+1] == '.' and matrix[i+1][j] == '.' and matrix[i+1][j+1] == '.':
            count[0] += 1
        elif matrix[i][j] == 'X' and matrix[i][j+1] == '.' and matrix[i+1][j] == '.' and matrix[i+1][j+1] == '.':
            count[1] += 1
        elif matrix[i][j] == '.' and matrix[i][j+1] == 'X' and matrix[i+1][j] == '.' and matrix[i+1][j+1] == '.':
            count[1] += 1
        elif matrix[i][j] == '.' and matrix[i][j+1] == '.' and matrix[i+1][j] == 'X' and matrix[i+1][j+1] == '.':
            count[1] += 1
        elif matrix[i][j] == '.' and matrix[i][j+1] == '.' and matrix[i+1][j] == '.' and matrix[i+1][j+1] == 'X':
            count[1] += 1
        elif matrix[i][j] == 'X' and matrix[i][j+1] == 'X' and matrix[i+1][j] == '.' and matrix[i+1][j+1] == '.':
            count[2] += 1
        elif matrix[i][j] == 'X' and matrix[i][j+1] == '.' and matrix[i+1][j] == 'X' and matrix[i+1][j+1] == '.':
            count[2] += 1
        elif matrix[i][j] == 'X' and matrix[i][j+1] == '.' and matrix[i+1][j] == '.' and matrix[i+1][j+1] == 'X':
            count[2] += 1
        elif matrix[i][j] == '.' and matrix[i][j+1] == 'X' and matrix[i+1][j] == 'X' and matrix[i+1][j+1] == '.':
            count[2] += 1
        elif matrix[i][j] == '.' and matrix[i][j+1] == 'X' and matrix[i+1][j] == '.' and matrix[i+1][j+1] == 'X':
            count[2] += 1
        elif matrix[i][j] == '.' and matrix[i][j+1] == '.' and matrix[i+1][j] == 'X' and matrix[i+1][j+1] == 'X':
            count[2] += 1
        elif matrix[i][j] == 'X' and matrix[i][j+1] == 'X' and matrix[i+1][j] == 'X' and matrix[i+1][j+1] == '.':
            count[3] += 1
        elif matrix[i][j] == 'X' and matrix[i][j+1] == 'X' and matrix[i+1][j] == '.' and matrix[i+1][j+1] == 'X':
            count[3] += 1
        elif matrix[i][j] == 'X' and matrix[i][j+1] == '.' and matrix[i+1][j] == 'X' and matrix[i+1][j+1] == 'X':
            count[3] += 1
        elif matrix[i][j] == '.' and matrix[i][j+1] == 'X' and matrix[i+1][j] == 'X' and matrix[i+1][j+1] == 'X':
            count[3] += 1
        elif matrix[i][j] == 'X' and matrix[i][j+1] == 'X' and matrix[i+1][j] == 'X' and matrix[i+1][j+1] == 'X':
            count[4] += 1

for i in range(5):
    print(count[i])
