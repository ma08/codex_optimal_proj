
# 
from sys import stdin

def main():
    N, M = [int(x) for x in stdin.readline().rstrip().split()]
    grid = [stdin.readline().rstrip() for _ in range(N)]
    for r in range(N - 1, -1, -1):
        for c in range(M):
            if grid[r][c] == 'V':
                if r + 1 < N and grid[r + 1][c] == '.':
                    grid[r + 1] = grid[r + 1][:c] + 'V' + grid[r + 1][c + 1:]
                if c - 1 >= 0 and grid[r][c - 1] == '.':
                    grid[r] = grid[r][:c - 1] + 'V' + grid[r][c:]
                if c + 1 < M and grid[r][c + 1] == '.':
                    grid[r] = grid[r][:c + 1] + 'V' + grid[r][c + 2:]
    for row in grid:
        print(row)

if __name__ == '__main__':
    main()
