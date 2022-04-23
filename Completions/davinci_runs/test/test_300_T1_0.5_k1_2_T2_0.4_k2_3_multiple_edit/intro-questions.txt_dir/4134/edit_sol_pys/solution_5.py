

def solve(n, m, k, grid, s, t):
    return 1

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    s = [input() for _ in range(k)]
    t = [input() for _ in range(k)]
    print(solve(n, m, k, grid, s, t))

if __name__ == '__main__':
    main()
