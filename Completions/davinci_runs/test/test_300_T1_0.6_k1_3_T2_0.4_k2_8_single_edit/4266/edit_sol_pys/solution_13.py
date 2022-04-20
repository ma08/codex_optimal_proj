

def main():
    """
    === MAIN ===
    """
    # Get input
    k, x = map(int, input().split())

    # Print out all possible x's, separated by spaces
    print(*range(x - k + 1, x + k))

if __name__ == "__main__":
    main()
