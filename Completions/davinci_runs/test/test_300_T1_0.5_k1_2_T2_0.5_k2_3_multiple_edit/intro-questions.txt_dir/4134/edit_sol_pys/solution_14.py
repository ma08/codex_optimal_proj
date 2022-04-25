

def solve(n, m, k, grid, start, end, p, q):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    p, q = map(int, input().split())
    print(solve(n, m, k, grid, start, end, p, q))

if __name__ == '__main__':
    main()
