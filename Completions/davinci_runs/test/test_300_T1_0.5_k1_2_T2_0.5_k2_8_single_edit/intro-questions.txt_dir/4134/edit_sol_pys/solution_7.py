import random

def solve(n, m, k, grid):
    return random.randint(0, 1)

def main():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, k, grid))

if __name__ == '__main__':
    main()
