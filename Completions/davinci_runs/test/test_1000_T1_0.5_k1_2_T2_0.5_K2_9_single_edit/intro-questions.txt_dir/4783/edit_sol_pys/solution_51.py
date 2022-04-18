

# Solution


def main():
    # Read Input
    M, N = [int(x) for x in input().strip().split()]
    heights = []
    for i in range(M):
        heights.append([int(x) for x in input().strip().split()])
    # Initialize Result Matrix
    result = [[0 for x in range(N)] for y in range(M)]
    # Fill First Row
    result[0][0] = heights[0][0]
    for i in range(1, N):
        result[0][i] = result[0][i-1] + heights[0][i]
    # Fill First Column
    for i in range(1, M):
        result[i][0] = result[i-1][0] + heights[i][0]
    # Fill Remaining Cells
    for i in range(1, M):
        for j in range(1, N):
            result[i][j] = min(result[i-1][j], result[i][j-1]) + heights[i][j]
    # Print Result
    print(result[M-1][N-1])

if __name__ == '__main__':
    main()
