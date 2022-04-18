

def main():
    # Read input
    M, N = [int(x) for x in input().split()]
    heights = [int(x) for x in input().split()]

    # Create a table with the minimum ladder lengths needed to get to each position
    # The first row and column are initialized to 0s, as they are the starting point
    table = [0] * N
    for i in range(1, N):
        # Find the minimum ladder length needed to get to the current position
        # from the possible adjacent positions
        table[i] = max(table[i-1], heights[i] - heights[i-1])

    # Print the minimum ladder length needed to get to the bottom right corner
    print(table[N-1])

if __name__ == '__main__':
    main()
