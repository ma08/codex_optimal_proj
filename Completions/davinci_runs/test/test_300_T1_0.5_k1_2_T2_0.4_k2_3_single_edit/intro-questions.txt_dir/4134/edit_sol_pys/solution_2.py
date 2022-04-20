

def solve(n, m, k, grid):
    return 1

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for i in range(n)]
    print(solve(n, m, k, grid))

if __name__ == '__main__':
    main()
