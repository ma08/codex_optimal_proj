

def solve(n, m, k, grid, dp):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0 for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n)]
    print(solve(n, m, k, grid, dp))

if __name__ == '__main__':
    main()
