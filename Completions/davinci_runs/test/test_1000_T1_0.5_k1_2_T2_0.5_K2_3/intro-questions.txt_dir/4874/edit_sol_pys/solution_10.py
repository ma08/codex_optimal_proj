

def main():
    N, M = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(N):
        grid.append(sys.stdin.readline().strip())
    moves = 0
    for i in range(M):
        if grid[0][i] == '_' or grid[0][i] == '#':
            moves += 1
    print(moves)

if __name__ == "__main__":
    main()
