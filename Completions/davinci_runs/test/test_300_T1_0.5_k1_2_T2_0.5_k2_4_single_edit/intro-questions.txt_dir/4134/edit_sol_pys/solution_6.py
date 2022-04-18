

def solve(n, m, k, grid):
    return 0

def main():
    n, m, k = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    print(solve(n, m, k, grid))

if __name__ == '__main__':
    main()
