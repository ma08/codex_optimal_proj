


def main():
    """
    Main function for this script
    :return: None
    """
    # Get input
    n = int(input())
    d = list(map(int, input().split()))

    # Set counter
    counter = 0

    # Run loop
    for k in range(1, max(d) + 1):
        if sum(1 for v in d if v >= k) == sum(1 for v in d if v < k):
            counter += 1

    # Print counter
    print(counter)


if __name__ == '__main__':
    main()