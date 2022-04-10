


def main():
    """
    Main function for this script
    :return: None
    """
    # Get input and split
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # Set variables
    total = 0
    counter = 1

    # Run loop to find total
    for i in range(n):
        if total + a[i] <= m:
            total += a[i]
        else:
            total = a[i]
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()
