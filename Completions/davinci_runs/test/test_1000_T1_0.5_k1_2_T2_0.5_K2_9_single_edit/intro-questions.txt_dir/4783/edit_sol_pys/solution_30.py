

def min_length(table, i, j, heights):
    # Find the minimum ladder length needed to get to the current position
    # from the possible adjacent positions
    return max(table[i-1][j], table[i][j-1], heights[i][j] - heights[i-1][j], heights[i][j] - heights[i][j-1])

def main():
    # Read input
    M, N = [int(x) for x in input().split()]
    heights = []
    for _ in range(M):
        heights.append([int(x) for x in input().split()])

    # Create a table with the minimum ladder lengths needed to get to each position
    # The first row and column are initialized to 0s, as they are the starting point
    table = [[0] * N for _ in range(M)]
    for i in range(1, M):
        for j in range(1, N):
            table[i][j] = min_length(table, i, j, heights)

    # Print the minimum ladder length needed to get to the bottom right corner
    print(table[M-1][N-1])

if __name__ == '__main__':
    main()
