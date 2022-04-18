

def solve(n, m, k, grid, visited):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                visited[i][j] = 1
                return 1
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, grid))

if __name__ == '__main__':
    main()
