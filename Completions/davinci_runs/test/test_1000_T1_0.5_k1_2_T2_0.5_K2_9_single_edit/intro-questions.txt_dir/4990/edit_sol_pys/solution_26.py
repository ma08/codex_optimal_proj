

def main():
    # Get input
    b = int(input())
    k = int(input())
    g = int(input())
    # Calculate number of days
    days = (b - 1) // (k - g + 1) + 1
    # Print result
    print(days)

if __name__ == '__main__':
    main()
