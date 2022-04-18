

def main():
    # Read input
    M, N = [int(x) for x in input().split()]  # type: int
    heights = []
    for _ in range(M):  # type: int
        heights.append([int(x) for x in input().split()])

    # Create a table with the minimum ladder lengths needed to get to each position
    # The first row and column are initialized to 0s, as they are the starting points
    table = [[0] * N for _ in range(M)]  # type: List[List[int]]
    for i in range(1, M):  # type: int
        for j in range(1, N):  # type: int
            # Find the maximum ladder length needed to get to the current position
            # from the possible adjacent positions
            table[i][j] = max(table[i-1][j], table[i][j-1], heights[i][j] - heights[i-1][j],
                              heights[i][j] - heights[i][j-1])

    # Print the minimum ladder length needed to get to the bottom right corner
    print(table[M-1][N-1])  # type: int

if __name__ == '__main__':
    main()
