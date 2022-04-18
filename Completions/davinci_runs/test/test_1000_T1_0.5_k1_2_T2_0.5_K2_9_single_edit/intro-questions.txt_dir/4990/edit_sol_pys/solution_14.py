
def main():
    # Get input
    b, k, g = [int(x) for x in input().split()]  # pylint: disable=C0103
    # Calculate number of days
    days = (b - 1) // (k - g + 1) + 1  # pylint: disable=C0103
    # Print result
    print(days)

if __name__ == '__main__':
    main()
