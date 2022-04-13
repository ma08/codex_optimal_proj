

def main():
    # Read input - Number of test cases
    T = int(input())
    for _ in range(T):
        # Read input - Number of elements in list
        N = int(input())
        # Read input - List
        L = [int(x) for x in input().split()]

        # Find the maximum ladder length needed to get to the bottom right corner
        print(find_max_ladder_length(L))

def find_max_ladder_length(L):
    # Create a table with the maximum ladder lengths needed to get to each position,
    # initialized to 0s, as they are the starting point
    table = [0] * len(L)
    for i in range(1, len(L)):
        # Find the maximum ladder length needed to get to the current position
        # from the possible adjacent positions
        table[i] = max(table[i-1], L[i] - L[i-1])

    # Return the maximum ladder length needed to get to the bottom right corner
    return table[len(L)-1]

if __name__ == '__main__':
    main()
