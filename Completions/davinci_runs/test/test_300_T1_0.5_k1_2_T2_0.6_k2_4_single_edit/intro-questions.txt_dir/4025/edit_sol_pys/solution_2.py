

def main():
    # Read in data
    n, k = [int(x) for x in input().split()]

    # Read in the heights
    heights = [int(x) for x in input().split()]

    # Find the maximum number of obstacles that can be jumped
    obstacles = 0
    for h in heights:
        if h + k <= 5:
            obstacles += 1

    # Print the result
    print(obstacles // 3)

if __name__ == "__main__":
    main()
