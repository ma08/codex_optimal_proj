

def main():
    M, N = map(int, input().split())
    heights = []
    for i in range(M):
        heights.append(list(map(int, input().split())))
    # heights = [[1, 2, 3], [6, 5, 4], [7, 8, 9]]]
    # heights = [[4, 3, 2, 1]]
    # print(heights)
    # print(len(heights))
    # print(len(heights[0]))

    # create a matrix of size MxN to store the max height possible at each position
    # initialize max_heights matrix with all 0
    max_heights = [[0 for i in range(N)] for j in range(M)]

    # initialize the first row of the max_heights matrix with the first row of heights matrix
    for i in range(N):
        max_heights[0][i] = heights[0][i]

    # initialize the first column of the max_heights matrix with the first column of heights matrix
    for i in range(M):
        max_heights[i][0] = heights[i][0]

    # iterate over the heights matrix
    # for each position calculate the maximum possible height
    # using the heights of the adjacent positions
    # by taking the minimum of the adjacent positions and adding 1
    # store the maximum possible height at that position in the max_heights matrix
    for i in range(1, M):
        for j in range(1, N):
            # print("i = {}, j = {}".format(i, j))
            max_heights[i][j] = min(max_heights[i][j-1], max_heights[i-1][j]) + 1

    # print(max_heights)

    # find the minimum of the last row of the max_heights matrix
    min_last_row = min(max_heights[M-1])

    # find the minimum of the last column of the max_heights matrix
    min_last_col = max_heights[0][N-1]
    for i in range(1, M):
        if max_heights[i][N-1] < min_last_col:
            min_last_col = max_heights[i][N-1]

    # print("min_last_row = {}".format(min_last_row))
    # print("min_last_col = {}".format(min_last_col))

    # find the minimum of the minimum of the last row and the last column
    min_last_row_col = min(min_last_row, min_last_col)

    # print(min_last_row_col)

    # subtract the minimum of the minimum of the last row and the last column from the height of the last position
    # which is the height of the coin
    ladder_length = heights[M-1][N-1] - min_last_row_col

    print(ladder_length)

main()
