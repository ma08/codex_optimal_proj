

import sys

def main():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    n, m = map(int, lines[0].split())
    matrix = [list(map(int, line.split())) for line in lines[1:]]
    res = solve(matrix, n, m)
    if res is None:
        print("NO")
    else:
        print("YES")
        print(res[0])
        print(res[1])

def solve(matrix, n, m):
    row_counts = [sum(row) for row in matrix]
    col_counts = [sum([matrix[i][j] for i in range(n)]) for j in range(m)]
    row_invert = [0 for _ in range(n)]
    col_invert = [0 for _ in range(m)]
    for i in range(n):
        if row_counts[i] > m / 2:
            row_invert[i] = 1
    for j in range(m):
        if col_counts[j] > n / 2:
            col_invert[j] = 1
    for i in range(n):
        for j in range(m):
            if row_invert[i] ^ col_invert[j] != matrix[i][j]:
                return None
    return ("".join(map(str, row_invert)), "".join(map(str, col_invert)))

if __name__ == "__main__":
    main()