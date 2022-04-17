

def solve(n, m, k, grid, arr):
    return 0

def main():
    arr = list(map(int, input().split()))
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, grid, arr))

if __name__ == '__main__':
    main()
