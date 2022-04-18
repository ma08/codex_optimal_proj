

def main():
    input_ = sys.stdin.readline
    N, M = map(int, input_().split())
    grid = []
    for _ in range(N):
        grid.append(input_().strip())
    moves = 0
    for i in range(M):
        if grid[0][i] == '_':
            moves += 1
    print(moves)

if __name__ == "__main__":
    main()
