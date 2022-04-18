
from sys import stdin

def main():
    N, M = [int(x) for x in stdin.readline().rstrip().split()]
    grid = [stdin.readline().rstrip() for _ in range(N)]
    for row in range(N - 1, -1, -1):
        for col in range(M):
            if grid[row][col] == 'V':
                if row + 1 < N and grid[row + 1][col] == '.':
                    grid[row + 1] = grid[row + 1][:col] + 'V' + grid[row + 1][col + 1:]
                if col - 1 >= 0 and grid[row][col - 1] == '.':
                    grid[row] = grid[row][:col - 1] + 'V' + grid[row][col:]
                if col + 1 < M and grid[row][col + 1] == '.':
                    grid[row] = grid[row][:col + 1] + 'V' + grid[row][col + 2:]
    for row in grid:
        print(row)

if __name__ == '__main__':
    main()
