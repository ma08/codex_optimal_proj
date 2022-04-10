

import sys
input = sys.stdin.readline

def main():
    n, m = [int(x) for x in input().split()]
    a = [[int(x) for x in input().split()] for _ in range(n)]
    row_invert = [0 for _ in range(n)]
    column_invert = [0 for _ in range(m)]
    for i in range(n):
        if sum(a[i]) == m:
            row_invert[i] = 1
    for j in range(m):
        if sum([a[i][j] for i in range(n)]) == n:
            column_invert[j] = 1
    if sum(row_invert) + sum(column_invert) != n + m:
        print("NO")
    else:
        print("YES")
        print("".join([str(x) for x in row_invert]))
        print("".join([str(x) for x in column_invert]))

if __name__ == "__main__":
    main()