

def main():
    """
    === MAIN ===
    """
    # Get input
    k, x = map(int, input().split())  # type: int

    # Print out all possible x's
    for i in range(k):  # type: int
        print(x - i, end=' ')
    for i in range(k):  # type: int
        print(x + i, end=' ')

if __name__ == "__main__":
    main()
