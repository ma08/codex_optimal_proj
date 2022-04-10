
def main():
    """
    Main function for this script
    :return: None
    """
    # Get input
    n = int(input())
    d = list(map(int, input().split()))

    # Run loop
    for k in range(1, max(d)):
        if sum(1 for v in d if v >= k) == sum(1 for v in d if v <= k):
            print(k)

    # Print max
    print(max(d))


if __name__ == '__main__':
    main()
