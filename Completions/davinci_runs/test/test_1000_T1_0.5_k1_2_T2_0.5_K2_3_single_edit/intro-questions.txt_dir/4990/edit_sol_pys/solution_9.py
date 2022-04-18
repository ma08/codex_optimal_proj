

def main():
    # Get input
    b, k, g = [int(x) for x in input().split()]
    # Calculate number of days
    days = (b - 1) // (k - g + 1) + 1
    # Print results
    print(f"{days} days")

if __name__ == '__main__':
    main()
