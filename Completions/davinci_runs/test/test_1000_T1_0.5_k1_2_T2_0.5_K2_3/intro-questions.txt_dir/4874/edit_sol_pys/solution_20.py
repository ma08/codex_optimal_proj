

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(input().strip())
    moves = []
    for i in range(M):
        if grid[0][i] == '_' or grid[0][i] == '#':
            moves.append(i)
    print(moves[0])

if __name__ == "__main__":
    main()
