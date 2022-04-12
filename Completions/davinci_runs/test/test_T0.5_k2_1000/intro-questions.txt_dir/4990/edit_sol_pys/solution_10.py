

def main():
    # Get input.
    b, k, g = [int(x) for x in input().split()] # read input
    # Calculate number of days.
    days = (b - 1) // (k - g + 1) + 1 # calculate days
    # Print result.
    print(days)

if __name__ == '__main__':
    main()
