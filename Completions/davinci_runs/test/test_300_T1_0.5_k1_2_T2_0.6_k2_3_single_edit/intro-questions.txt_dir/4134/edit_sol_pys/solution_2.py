

def solve(n, m, k, p, grid):
    return n * m

def main():
    n, m, k, p = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, p, grid))

if __name__ == '__main__':
    main()
