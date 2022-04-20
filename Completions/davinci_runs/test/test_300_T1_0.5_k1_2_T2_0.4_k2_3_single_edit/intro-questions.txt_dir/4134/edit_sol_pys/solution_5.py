

def solve(n, m, k, grid, cnt):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    print(solve(n, m, k, grid, cnt))

if __name__ == '__main__':
    main()
