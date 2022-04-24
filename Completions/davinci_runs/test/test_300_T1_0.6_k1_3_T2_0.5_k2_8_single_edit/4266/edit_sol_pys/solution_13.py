

def main():
    """
    === MAIN ===
    """
    # Get input
    n, m = map(int, input().split())

    # Print out all possible m's
    for i in range(n):
        print(m - i, end=' ')
    for i in range(n):
        print(m + i, end=' ')

if __name__ == "__main__":
    main()
