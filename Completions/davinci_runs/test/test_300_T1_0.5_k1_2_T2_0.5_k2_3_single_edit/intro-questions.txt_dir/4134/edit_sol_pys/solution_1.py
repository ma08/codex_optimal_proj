

    # for i, row in enumerate(grid):
    #     for j, cell in enumerate(row):
    #         if cell == 1:
    #             if i > 0 and grid[i-1][j] == 0:
    #                 return 1
    #             if j > 0 and grid[i][j-1] == 0:
    #                 return 1
    #             if i < n-1 and grid[i+1][j] == 0:
    #                 return 1
    #             if j < m-1 and grid[i][j+1] == 0:
    #                 return 1
    # return 0
def solve(n, m, k, grid):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, grid))

if __name__ == '__main__':
    main()
