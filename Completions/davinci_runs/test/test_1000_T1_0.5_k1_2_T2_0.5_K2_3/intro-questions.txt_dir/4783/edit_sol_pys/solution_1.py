

def main():
    M, N = map(int, input().split())
    heights = []
    for i in range(M):
        heights.append(list(map(int, input().split())))

    # create a matrix of size MxN to store the minimum height possible at each position
    # initialize min_heights matrix with all 0
    min_heights = [[0 for i in range(N)] for j in range(M)]

    # initialize the first row of the min_heights matrix with the first row of heights matrix
    for i in range(N):
        min_heights[0][i] = heights[0][i]

    # initialize the first column of the min_heights matrix with the first column of heights matrix
    for i in range(M):
        min_heights[i][0] = heights[i][0]

    # iterate over the heights matrix
    # for each position calculate the maximum possible height
    # using the heights of the adjacent positions
    # by taking the minimum of the adjacent positions and adding 1
    # store the minimum possible height at that position in the min_heights matrix
    for i in range(1, M):
        for j in range(1, N):
            min_heights[i][j] = min(min_heights[i][j-1], min_heights[i-1][j]) + 1

    # find the minimum of the last row of the min_heights matrix
    min_last_row = min(min_heights[M-1])

    # find the minimum of the last column of the min_heights matrix manually
    min_last_col = min_heights[0][N-1]
    for i in range(1, M):
        if min_heights[i][N-1] < min_last_col:
            min_last_col = min_heights[i][N-1]

    # find the minimum of the minimum of the last row and the last column
    min_last_row_col = min(min_last_row, min_last_col)

    # print(min_last_row_col)

    # subtract the minimum of the minimum of the last row and the last column from the height of the last position
    # which is the height of the coin
    ladder_length = heights[M-1][N-1] - min_last_row_col

    print(ladder_length)

main()
