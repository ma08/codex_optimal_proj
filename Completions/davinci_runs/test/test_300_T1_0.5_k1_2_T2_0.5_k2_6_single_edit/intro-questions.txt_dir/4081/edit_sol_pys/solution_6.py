import sys
import os

def print_matrix(matrix):
    for row in matrix:
        print(row)

def get_matrix(n, m):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(0)
    return matrix

def main():
    n, m = [int(x) for x in input().split()]
    matrix = get_matrix(n, m)

    for i in range(n):
        row = [int(x) for x in input().split()]
        for j in range(m):
            matrix[i][j] = row[j]

    print_matrix(matrix)

    max_sum = 0
    max_sum_idx = [-1, -1]

    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0:
                matrix[i][j] += max([matrix[i-1][j], matrix[i][j-1]])
            elif i > 0:
                matrix[i][j] += matrix[i-1][j]
            elif j > 0:
                matrix[i][j] += matrix[i][j-1]

    print_matrix(matrix)

    print(matrix[n-1][m-1])

    path = []
    i, j = n-1, m-1
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if matrix[i-1][j] > matrix[i][j-1]:
                path.append('U')
                i -= 1
            else:
                path.append('L')
                j -= 1
        elif i > 0:
            path.append('U')
            i -= 1
        elif j > 0:
            path.append('L')
            j -= 1

    path.reverse()
    print(''.join(path))

if __name__ == '__main__':
    main()
