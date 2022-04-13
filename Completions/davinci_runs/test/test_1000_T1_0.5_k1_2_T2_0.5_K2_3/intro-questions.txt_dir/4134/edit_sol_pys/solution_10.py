

def solve(n, m, k, grid, dp, dx, dy):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print(solve(n, m, k, grid, dp, dx, dy))

if __name__ == '__main__':
    main()
