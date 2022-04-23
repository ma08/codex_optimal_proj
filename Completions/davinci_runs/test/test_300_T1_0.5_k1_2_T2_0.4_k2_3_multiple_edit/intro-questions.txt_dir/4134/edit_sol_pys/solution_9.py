

def solve(n, m, k, grid, s):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [input() for _ in range(n)]
    s = [input() for _ in range(k)]
    print(solve(n, m, k, grid, s))

if __name__ == '__main__':
    main()
