def main():
    # Read input
    N = int(input())
    heights = [int(x) for x in input().split()]


    # Initialize the minimum ladder length needed to get to the first position to 0
    table = [0]

    for i in range(1, N):
        # Find the maximum ladder length needed to get to the current position
        # from the possible adjacent positions
        table.append(max(table[i-1], heights[i] - heights[i-1]))

    # Print the minimum ladder length needed to get to the last position
    print(table[N-1])

if __name__ == '__main__':
    main()
