

def solve(n, m, grid):
    return 0

def main():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, grid))

if __name__ == '__main__':
    main()
