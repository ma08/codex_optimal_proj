

def solve(n, m, k, grid, a, b):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    a, b = map(int, input().split())
    print(solve(n, m, k, grid, a, b))

if __name__ == '__main__':
    main()
