

def main():
    """
    === MAIN ===
    """
    # Get input from user
    k, x = map(int, input().split()) # Get input

    # Print out all possible x's
    for i in range(1, k):
        print(x - i, end=' ')
    for i in range(k):
        print(x + i, end=' ')

if __name__ == "__main__":
    main()
