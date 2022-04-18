

def solve(n, m, k, grid, max_num):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    max_num = max(max(row) for row in grid)
    print(solve(n, m, k, grid, max_num))

if __name__ == '__main__':
    main()
