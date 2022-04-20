

def main():
    """
    === MAIN ===
    """
    # Get input
    k, x = map(int, input().split())

    # Print out all possible x's
    for i in range(k-1):
        print(x - k + i, end=' ')
    print(x)
    for i in range(k-1):
        print(x + i + 1, end=' ')
    print(x + k)

if __name__ == "__main__":
    main()
