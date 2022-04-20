import sys


def main():
    """
    === MAIN ===
    """
    # Get input from stdin
    k, x = map(int, sys.stdin.readline().split())

    # Print out all possible x's
    for i in range(1, k):
        print(x - i, end=' ')
    for i in range(1, k):
        print(x + i, end=' ')

if __name__ == "__main__":
    main()
