

def main():
    N, M = map(int, input().strip().split()) # read input and split
    grid = []
    for _ in range(N):
        grid.append(input().strip()) # append the input to grid
    moves = 0
    for i in range(M):
        if grid[0][i] == '_':
            moves += 1
    print(moves)

if __name__ == "__main__":
    main()
