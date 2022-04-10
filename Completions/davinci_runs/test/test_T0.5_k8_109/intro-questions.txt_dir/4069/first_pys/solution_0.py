


def main():
    """
    The key to solving this problem is to find the remainder of X after moving K times
    """
    # get inputs
    X, K, D = map(int, input().split())

    # get the remainder of X after moving K times
    r = abs(X) % D

    # if the remainder is smaller than the distance to move
    if r < D - r:
        print(r)
    else:
        print(D - r)


if __name__ == "__main__":
    main()