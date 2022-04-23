from collections import deque

def solve(n, m, k, grid):
    return 0

def main():
    n, m, k = map(int, input().split())  # n: height, m: width, k: max distance
    grid = [list(map(int, input().split())) for _ in range(n)]  # grid[y][x]
    print(solve(n, m, k, grid))

if __name__ == '__main__':
    main()
