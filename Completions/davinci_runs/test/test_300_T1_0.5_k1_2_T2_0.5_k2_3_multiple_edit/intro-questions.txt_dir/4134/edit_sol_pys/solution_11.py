

def solve(n, m, k, mat, r, c):
    if n == 1 and m == 1:
        return 0
    if r == n - 1 and c == m - 1:
        return 0
    if r == n - 1:
        return solve(n, m, k, mat, r, c + 1)
    if c == m - 1:
        return solve(n, m, k, mat, r + 1, c)
    if mat[r + 1][c] > mat[r][c + 1]:
        return 1 + solve(n, m, k, mat, r, c + 1)
    else:
        return 1 + solve(n, m, k, mat, r + 1, c)

def main():
    n, m, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, mat, 0, 0))

if __name__ == '__main__':
    main()
