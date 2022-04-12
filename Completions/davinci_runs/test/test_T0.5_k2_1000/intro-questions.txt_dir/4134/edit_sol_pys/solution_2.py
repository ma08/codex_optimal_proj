

def solve(n, k, grid):
    return 0

def main():
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)] 
    print(solve(n, k, grid))

if __name__ == '__main__':
    main()
