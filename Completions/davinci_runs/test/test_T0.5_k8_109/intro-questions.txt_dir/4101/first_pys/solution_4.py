

import sys

def is_sorted(matrix):
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            if i == n - 1 and j == m - 1:
                break
            if matrix[i][j] > matrix[i][j + 1]:
                return False
    return True

def main():
    n, m = map(int, sys.stdin.readline().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, sys.stdin.readline().split())))

    rows = [0] * n
    cols = [0] * m

    for i in range(n):
        for j in range(m):
            if i == 0:
                continue
            if matrix[i][j] < matrix[i - 1][j]:
                rows[i] = 1
                break

    for j in range(m):
        for i in range(n):
            if j == 0:
                continue
            if matrix[i][j] < matrix[i][j - 1]:
                cols[j] = 1
                break

    for i in range(n):
        for j in range(m):
            if i == n - 1 and j == m - 1:
                break
            if matrix[i][j] > matrix[i][j + 1]:
                if rows[i] == 0:
                    rows[i] = 1
                else:
                    print("NO")
                    return
            if matrix[i][j] > matrix[i + 1][j]:
                if cols[j] == 0:
                    cols[j] = 1
                else:
                    print("NO")
                    return

    print("YES")
    print("".join(map(str, rows)))
    print("".join(map(str, cols)))

if __name__ == '__main__':
    main()