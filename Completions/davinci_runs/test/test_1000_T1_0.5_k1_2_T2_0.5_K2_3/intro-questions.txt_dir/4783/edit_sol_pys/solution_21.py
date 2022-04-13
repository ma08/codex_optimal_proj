

def main():
    # Read input
    M, N = [int(x) for x in input().split()]
    heights = []
    for _ in range(M):
        heights.append([int(x) for x in input().split()])

    # Create a table with the maximum ladder lengths needed to get to each position
    # The first row and column are initialized to 0s, as they are the starting point
    table = [[0] * N for _ in range(M)]
    for i in range(1, M):
        for j in range(1, N):
            # Find the maximum ladder length needed to get to the current position
            # from the possible adjacent positions
            table[i][j] = max(table[i-1][j], table[i][j-1], abs(heights[i][j] - heights[i-1][j]), abs(heights[i][j] - heights[i][j-1]))

    # Print the maximum ladder length needed to get to the bottom right corner
    print(table[M-1][N-1])

if __name__ == '__main__':
    main()
