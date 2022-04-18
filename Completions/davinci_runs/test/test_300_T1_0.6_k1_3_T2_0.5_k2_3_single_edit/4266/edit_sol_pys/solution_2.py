

def main():
    """
    === MAIN ===
    """
    # Get input
    k, x = map(int, input().split())

    # Print out all possible x's
    for i in range(k):
        print(x - k + i + 1, end=' ')

if __name__ == "__main__":
    main()
