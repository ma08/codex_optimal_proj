

def main():
    # Get input
    a, b, c = [int(x) for x in input().split()]
    # Calculate number of days
    days = int(c / (a - b)) + 1
    # Print result
    print(days)

if __name__ == '__main__':
    main()
