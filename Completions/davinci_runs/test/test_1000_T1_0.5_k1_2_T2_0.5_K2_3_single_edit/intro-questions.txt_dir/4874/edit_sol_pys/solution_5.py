import sys

def main():
    i = sys.stdin.readline
    N, M = map(int, i().split())
    grid = []
    for _ in range(N):
        grid.append(i().strip())
    moves = 0
    for i in range(M):
        if grid[0][i] == '_':
            moves += 1
    print(moves)

if __name__ == "__main__":
    main()
