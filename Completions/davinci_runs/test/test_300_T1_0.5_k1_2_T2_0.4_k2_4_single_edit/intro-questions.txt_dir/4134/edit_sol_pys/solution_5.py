import sys

def solve(n, m, k, grid):
    return 0

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(solve(n, m, k, grid))

if __name__ == '__main__':
    main()
