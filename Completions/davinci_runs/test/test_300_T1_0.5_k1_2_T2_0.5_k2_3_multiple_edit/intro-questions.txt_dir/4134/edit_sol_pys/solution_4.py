

def solve(n, m, k, grid, start, end, dirs):
    return

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    print(solve(n, m, k, grid, start, end, dirs))

if __name__ == '__main__':
    main()
