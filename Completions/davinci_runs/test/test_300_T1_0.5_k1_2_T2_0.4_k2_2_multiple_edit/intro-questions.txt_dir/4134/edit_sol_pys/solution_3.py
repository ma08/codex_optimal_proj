

def solve(n, m, grid, visited):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    print(solve(n, m, grid, visited))

if __name__ == '__main__':
    main()
