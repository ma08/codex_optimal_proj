

def main():
    # Get input from user
    b, k, g = [int(x) for x in input().split()]  # Get input from user
    days = (b - 1) // (k - g + 1) + 1  # Calculate number of days
    print(days)  # Print result

if __name__ == '__main__':
    main()
