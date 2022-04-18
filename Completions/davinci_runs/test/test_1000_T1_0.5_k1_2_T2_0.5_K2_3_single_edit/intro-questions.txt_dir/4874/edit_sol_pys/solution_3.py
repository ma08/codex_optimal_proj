import sys

def main():
    print(input())
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input().strip())
    moves = 0
    for i in range(M):
        if grid[0][i] == '_':
            moves += 1
    print(moves, end="")

if __name__ == "__main__":
    main()
