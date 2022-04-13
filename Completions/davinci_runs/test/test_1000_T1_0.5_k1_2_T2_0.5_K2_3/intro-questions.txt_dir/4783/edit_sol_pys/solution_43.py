

def main():
    M, N = [int(i) for i in input().split()]
    heights = [[int(i) for i in input().split()] for i in range(M)]

    ladder_lengths = [[0 for i in range(N)] for i in range(M)]
    for i in range(N):
        ladder_lengths[0][i] = max(heights[0][i], heights[0][i-1])
    for i in range(M):
        ladder_lengths[i][0] = max(heights[i][0], heights[i-1][0])

    #Fill in the rest of the ladder_lengths array
    #For each position, we want to find the minimum length of ladder needed to reach the position
    #We can either come from the left or the top, so we take the minimum of the two
    #Then we add the difference between the height of the current and previous positions
    #The difference is the minimum length of ladder needed to reach the current position
    for i in range(1, M):
        for j in range(1, N):
            ladder_lengths[i][j] = min(ladder_lengths[i-1][j], ladder_lengths[i][j-1]) + max(heights[i][j] - heights[i-1][j], heights[i][j] - heights[i][j-1])

    #Output the minimum length of ladder needed to reach the bottom right position
    print(ladder_lengths[M-1][N-1])

main()
