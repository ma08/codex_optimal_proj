
def main():
    # Get input
    k, x = map(int, input().split())

    # Print out all possible x's
    for i in range(1, k + 1):
        print(x - i, end=' ')
    for i in range(1, k + 1):
        print(x + i, end=' ') 


if __name__ == "__main__":
    main()
